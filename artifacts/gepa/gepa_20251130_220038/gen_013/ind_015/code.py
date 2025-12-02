
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.125),     # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.125),   # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.125),    # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.125)    # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums for bars 2-4
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + beat * 0.375, end=bar_start + beat * 0.375 + 0.375)
        drums.notes.append(kick)
    # Snare on 2 and 4
    for beat in [1, 3]:
        snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat * 0.375, end=bar_start + beat * 0.375 + 0.375)
        drums.notes.append(snare)
    # Hihat on every eighth
    for beat in range(0, 4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + beat * 0.375, end=bar_start + beat * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (20, 1.5, 0.375),     # F
    (21, 1.875, 0.375),   # F#
    (20, 2.25, 0.375),    # F
    (19, 2.625, 0.375),   # E
    # Bar 3
    (18, 3.0, 0.375),     # D
    (19, 3.375, 0.375),   # E
    (20, 3.75, 0.375),    # F
    (21, 4.125, 0.375),   # F#
    # Bar 4
    (20, 4.5, 0.375),     # F
    (19, 4.875, 0.375),   # E
    (18, 5.25, 0.375),    # D
    (17, 5.625, 0.375)    # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = []
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # 7th chord on 2
    if bar == 2:
        # Fm7: F, Ab, C, Eb
        for pitch in [20, 23, 24, 27]:
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.75, end=bar_start + 1.125))
    elif bar == 3:
        # Bb7: Bb, D, F, Ab
        for pitch in [21, 25, 27, 23]:
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.75, end=bar_start + 1.125))
    elif bar == 4:
        # Eb7: Eb, G, Bb, Db
        for pitch in [27, 29, 21, 24]:
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.75, end=bar_start + 1.125))

for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - short motif, make it sing
# Motif: F, Ab, G, Eb
sax_notes = [
    (20, 1.5, 0.375),
    (23, 1.875, 0.375),
    (22, 2.25, 0.375),
    (27, 2.625, 0.375),
    (20, 3.0, 0.375),
    (23, 3.375, 0.375),
    (22, 3.75, 0.375),
    (27, 4.125, 0.375),
    (20, 4.5, 0.375),
    (23, 4.875, 0.375),
    (22, 5.25, 0.375),
    (27, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_intro.mid')
