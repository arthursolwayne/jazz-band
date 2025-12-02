
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
    (36, 0.0, 1.5),  # Kick on 1
    (38, 0.75, 1.5), # Snare on 2
    (36, 1.125, 1.5),# Kick on 3
    (38, 1.5, 1.5),  # Snare on 4
    (42, 0.0, 1.5),  # Hihat on every eighth
    (42, 0.375, 1.5),
    (42, 0.75, 1.5),
    (42, 1.125, 1.5),
    (42, 1.5, 1.5)
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Roots and fifths with chromatic approaches
# Fm: F, C, Ab, D
bass_notes = [
    (53, 1.5, 1.875), # F2 (root)
    (55, 1.875, 2.25), # G2 (chromatic approach to Ab)
    (51, 2.25, 2.625), # Ab2 (fifth)
    (53, 2.625, 3.0), # F2 (root)
    (53, 3.0, 3.375), # F2
    (55, 3.375, 3.75), # G2 (chromatic approach to Ab)
    (51, 3.75, 4.125), # Ab2
    (53, 4.125, 4.5), # F2
    (53, 4.5, 4.875), # F2
    (55, 4.875, 5.25), # G2
    (51, 5.25, 5.625), # Ab2
    (53, 5.625, 6.0) # F2
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 1.5), # F
    (56, 1.5, 1.5), # Ab
    (58, 1.5, 1.5), # C
    (60, 1.5, 1.5), # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 2.25, 2.25), # Bb
    (62, 2.25, 2.25), # D
    (53, 2.25, 2.25), # F
    (56, 2.25, 2.25), # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (52, 3.0, 3.0), # Eb
    (55, 3.0, 3.0), # G
    (58, 3.0, 3.0), # Bb
    (60, 3.0, 3.0), # D
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (66, 1.5, 1.875), # G (start of motif)
    (69, 1.875, 2.25), # Bb
    (66, 2.25, 2.625), # G (return)
    (69, 2.625, 3.0), # Bb
    (71, 3.0, 3.375), # C
    (69, 3.375, 3.75), # Bb
    (66, 3.75, 4.125), # G
    (69, 4.125, 4.5), # Bb
    (71, 4.5, 4.875), # C
    (69, 4.875, 5.25), # Bb
    (66, 5.25, 5.625), # G
    (69, 5.625, 6.0) # Bb (resolve)
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
