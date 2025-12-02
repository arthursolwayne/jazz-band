
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1 & 2
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2 & 3
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line in Fm, chromatic approaches)
bass_notes = [
    (44, 1.5, 0.375),   # F (root)
    (45, 1.875, 0.375),  # Gb (chromatic approach)
    (46, 2.25, 0.375),   # Ab (3rd)
    (47, 2.625, 0.375),  # Bb (4th)
    (45, 3.0, 0.375),    # Gb (chromatic)
    (46, 3.375, 0.375),  # Ab (3rd)
    (47, 3.75, 0.375),   # Bb (4th)
    (48, 4.125, 0.375),  # B (5th)
    (46, 4.5, 0.375),    # Ab (3rd)
    (47, 4.875, 0.375),  # Bb (4th)
    (48, 5.25, 0.375),   # B (5th)
    (49, 5.625, 0.375)   # C (6th)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    (48, 1.875, 0.1875), # C7 on 2
    (50, 1.875, 0.1875),
    (52, 1.875, 0.1875),
    (53, 1.875, 0.1875),
    (48, 2.625, 0.1875), # C7 on 4
    (50, 2.625, 0.1875),
    (52, 2.625, 0.1875),
    (53, 2.625, 0.1875),
    (48, 3.375, 0.1875), # C7 on 2
    (50, 3.375, 0.1875),
    (52, 3.375, 0.1875),
    (53, 3.375, 0.1875),
    (48, 4.125, 0.1875), # C7 on 4
    (50, 4.125, 0.1875),
    (52, 4.125, 0.1875),
    (53, 4.125, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Little Ray (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375))
    # Snare on 2 and 4
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375))
    # Hihat on every eighth
    for beat in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1875))

# Sax: Dante (short motif, start on bar 2, leave it hanging, come back on bar 4)
# Motif: F - Ab - Bb - F
sax_notes = [
    (44, 1.5, 0.375),   # F
    (46, 1.875, 0.375),  # Ab
    (47, 2.25, 0.375),   # Bb
    (44, 2.625, 0.375),  # F (hangs)
    (44, 4.5, 0.375),    # F (return)
    (46, 4.875, 0.375),  # Ab
    (47, 5.25, 0.375),   # Bb
    (44, 5.625, 0.375)   # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
