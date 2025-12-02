
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (33, 1.5, 0.375),  # F
    (31, 1.875, 0.375), # Eb
    (30, 2.25, 0.375),  # D
    (28, 2.625, 0.375), # C
    (33, 3.0, 0.375),   # F
    (31, 3.375, 0.375), # Eb
    (30, 3.75, 0.375),  # D
    (28, 4.125, 0.375), # C
    (33, 4.5, 0.375),   # F
    (31, 4.875, 0.375), # Eb
    (30, 5.25, 0.375),  # D
    (28, 5.625, 0.375)  # C
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (61, 1.5, 0.375),   # F7: F, A, C, Eb
    (64, 1.5, 0.375),
    (60, 1.5, 0.375),
    (62, 1.5, 0.375),
    # Bar 3
    (61, 3.0, 0.375),
    (64, 3.0, 0.375),
    (60, 3.0, 0.375),
    (62, 3.0, 0.375),
    # Bar 4
    (61, 4.5, 0.375),
    (64, 4.5, 0.375),
    (60, 4.5, 0.375),
    (62, 4.5, 0.375)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875))

# Dante: Tenor sax intro - one short motif, make it sing
# Fm scale: F, Gb, Ab, A, Bb, B, C
sax_notes = [
    (64, 1.5, 0.375),  # F
    (63, 1.875, 0.375), # Gb
    (61, 2.25, 0.375),  # Ab
    (62, 2.625, 0.375), # A
    (60, 3.0, 0.375),   # Bb
    (61, 3.375, 0.375), # Ab
    (64, 3.75, 0.375),  # F
    (65, 4.125, 0.375), # B
    (64, 4.5, 0.375),   # F
    (63, 4.875, 0.375), # Gb
    (61, 5.25, 0.375),  # Ab
    (62, 5.625, 0.375)  # A
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
