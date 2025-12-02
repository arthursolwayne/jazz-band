
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.1875, 0.1875),
    (36, 0.75, 0.375),  # Kick on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (42, 0.9375, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (61, 1.875, 0.375), # C
    (63, 2.25, 0.375),  # D
    (65, 2.625, 0.375), # F
    (64, 3.0, 0.375),   # E
    (62, 3.375, 0.375), # D
    (60, 3.75, 0.375),  # C
    (62, 4.125, 0.375), # D
    (63, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # E
    (65, 5.25, 0.375),  # F
    (67, 5.625, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Dm7, F7, Bb7, G7
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375),  # D
    (67, 1.5, 0.375),  # G
    (69, 1.5, 0.375),  # Bb
    (64, 1.5, 0.375),  # F
    (62, 2.25, 0.375), # D
    (67, 2.25, 0.375), # G
    (71, 2.25, 0.375), # B
    (69, 2.25, 0.375), # A
    # Bar 3 (3.0 - 4.5s)
    (65, 3.0, 0.375),  # F
    (70, 3.0, 0.375),  # A
    (72, 3.0, 0.375),  # B
    (67, 3.0, 0.375),  # G
    (65, 3.75, 0.375), # F
    (70, 3.75, 0.375), # A
    (74, 3.75, 0.375), # D
    (72, 3.75, 0.375), # B
    # Bar 4 (4.5 - 6.0s)
    (67, 4.5, 0.375),  # G
    (72, 4.5, 0.375),  # B
    (74, 4.5, 0.375),  # D
    (76, 4.5, 0.375),  # F#
    (67, 5.25, 0.375), # G
    (72, 5.25, 0.375), # B
    (74, 5.25, 0.375), # D
    (76, 5.25, 0.375)  # F#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody in Dm, one short motif, make it sing
sax_notes = [
    (65, 1.5, 0.375),  # F
    (62, 2.25, 0.375), # D
    (67, 3.0, 0.375),  # G
    (65, 3.75, 0.375), # F
    (64, 4.5, 0.375),  # E
    (62, 5.25, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
