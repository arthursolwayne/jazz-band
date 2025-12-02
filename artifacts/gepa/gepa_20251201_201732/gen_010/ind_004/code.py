
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    (62, 1.5, 1.75),  # D2 on 1
    (67, 1.75, 2.0),  # G2 on 2
    (64, 2.0, 2.25),  # E2 (chromatic approach on 3)
    (62, 2.25, 2.5),  # D2 on 4
    (67, 2.5, 2.75),  # G2 on 1
    (72, 2.75, 3.0),  # B2 (chromatic approach on 2)
    (67, 3.0, 3.25),  # G2 on 3
    (64, 3.25, 3.5),  # E2 (chromatic approach on 4)
    (62, 3.5, 3.75),  # D2 on 1
    (67, 3.75, 4.0),  # G2 on 2
    (72, 4.0, 4.25),  # B2 (chromatic approach on 3)
    (69, 4.25, 4.5),  # A2 (chromatic approach on 4)
    (67, 4.5, 4.75),  # G2 on 1
    (72, 4.75, 5.0),  # B2 on 2
    (69, 5.0, 5.25),  # A2 on 3
    (67, 5.25, 5.5),  # G2 on 4
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = [
    (62, 1.5, 1.75),  # D
    (67, 1.5, 1.75),  # A
    (64, 1.5, 1.75),  # F#
    (69, 1.5, 1.75),  # C#
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    (67, 2.0, 2.25),  # G
    (71, 2.0, 2.25),  # Bb
    (69, 2.0, 2.25),  # D
    (65, 2.0, 2.25),  # F
])
# Bar 4: Bm7 (B D# F# A)
piano_notes.extend([
    (69, 2.5, 2.75),  # B
    (74, 2.5, 2.75),  # D#
    (71, 2.5, 2.75),  # F#
    (67, 2.5, 2.75),  # A
])
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D - F# - G - D (3rd, 5th, 6th, root)
sax_notes = [
    (62, 1.5, 1.75),  # D
    (67, 1.75, 2.0),  # F#
    (69, 2.0, 2.25),  # G
    (62, 2.25, 2.5),  # D (hang)
    (62, 3.5, 3.75),  # D (return)
    (67, 3.75, 4.0),  # F#
    (69, 4.0, 4.25),  # G
    (62, 4.25, 4.5)   # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 2.5s)
    (36, 1.5, 1.875),  # Kick on 1
    (42, 1.5, 1.6875), # Hihat on 1
    (38, 1.875, 2.125), # Snare on 2
    (42, 1.875, 2.0625), # Hihat on 2
    (36, 2.25, 2.625),  # Kick on 3
    (42, 2.25, 2.4375), # Hihat on 3
    (38, 2.625, 2.875), # Snare on 4
    (42, 2.625, 2.8125), # Hihat on 4

    # Bar 3 (2.5 - 3.5s)
    (36, 2.5, 2.875),  # Kick on 1
    (42, 2.5, 2.6875), # Hihat on 1
    (38, 2.875, 3.125), # Snare on 2
    (42, 2.875, 3.0625), # Hihat on 2
    (36, 3.25, 3.625),  # Kick on 3
    (42, 3.25, 3.4375), # Hihat on 3
    (38, 3.625, 3.875), # Snare on 4
    (42, 3.625, 3.8125), # Hihat on 4

    # Bar 4 (3.5 - 4.5s)
    (36, 3.5, 3.875),  # Kick on 1
    (42, 3.5, 3.6875), # Hihat on 1
    (38, 3.875, 4.125), # Snare on 2
    (42, 3.875, 4.0625), # Hihat on 2
    (36, 4.25, 4.625),  # Kick on 3
    (42, 4.25, 4.4375), # Hihat on 3
    (38, 4.625, 4.875), # Snare on 4
    (42, 4.625, 4.8125) # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
