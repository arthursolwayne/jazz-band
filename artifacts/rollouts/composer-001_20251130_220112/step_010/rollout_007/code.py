
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &
    (36, 1.5, 0.375)  # Kick on 3
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, never the same note twice
bass_notes = [
    (35, 1.5, 0.375),   # F (root)
    (36, 1.875, 0.375),  # Gb (chromatic approach)
    (34, 2.25, 0.375),   # Eb (3rd)
    (33, 2.625, 0.375),  # D (chromatic approach)
    (31, 3.0, 0.375),    # C (5th)
    (30, 3.375, 0.375),  # Bb (chromatic approach)
    (29, 3.75, 0.375),   # Ab (7th)
    (28, 4.125, 0.375),  # G (chromatic approach)
    (35, 4.5, 0.375),    # F (root)
    (36, 4.875, 0.375),  # Gb (chromatic approach)
    (34, 5.25, 0.375),   # Eb (3rd)
    (33, 5.625, 0.375)   # D (chromatic approach)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7: F, Ab, C, Eb
# Bbm7: Bb, Db, F, Ab
piano_notes = [
    # Bar 2
    (53, 1.5, 0.375),  # F
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # Eb
    (65, 1.5, 0.375),  # Ab
    (50, 2.25, 0.375),  # Bb
    (57, 2.25, 0.375),  # F
    (60, 2.25, 0.375),  # Ab
    (64, 2.25, 0.375),  # Db
    # Bar 3
    (53, 3.0, 0.375),  # F
    (60, 3.0, 0.375),  # C
    (64, 3.0, 0.375),  # Eb
    (65, 3.0, 0.375),  # Ab
    (50, 3.75, 0.375),  # Bb
    (57, 3.75, 0.375),  # F
    (60, 3.75, 0.375),  # Ab
    (64, 3.75, 0.375),  # Db
    # Bar 4
    (53, 4.5, 0.375),  # F
    (60, 4.5, 0.375),  # C
    (64, 4.5, 0.375),  # Eb
    (65, 4.5, 0.375),  # Ab
    (50, 5.25, 0.375),  # Bb
    (57, 5.25, 0.375),  # F
    (60, 5.25, 0.375),  # Ab
    (64, 5.25, 0.375)   # Db
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, C, Eb -> play F Ab C Eb (3 notes, leave Eb hanging)
# Then repeat with F, Bb, C, F -> F Bb C F (3 notes, leave F hanging)

sax_notes = [
    (53, 1.5, 0.375),  # F
    (65, 1.875, 0.375), # Ab
    (60, 2.25, 0.375),  # C
    (64, 2.625, 0.375), # Eb
    (53, 3.0, 0.375),   # F
    (50, 3.375, 0.375), # Bb
    (60, 3.75, 0.375),  # C
    (53, 4.125, 0.375)  # F
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
