
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (65, 2.25, 0.375), (67, 2.625, 0.375),
    (69, 3.0, 0.375), (71, 3.375, 0.375), (72, 3.75, 0.375), (74, 4.125, 0.375),
    (76, 4.5, 0.375), (77, 4.875, 0.375), (79, 5.25, 0.375), (81, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    b = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(b)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 0.375), (67, 1.5, 0.375), (72, 1.5, 0.375), (76, 1.5, 0.375),  # D7
    (64, 2.25, 0.375), (67, 2.25, 0.375), (72, 2.25, 0.375), (76, 2.25, 0.375),  # D7
    # Bar 3
    (64, 3.0, 0.375), (67, 3.0, 0.375), (72, 3.0, 0.375), (76, 3.0, 0.375),  # D7
    (64, 3.75, 0.375), (67, 3.75, 0.375), (72, 3.75, 0.375), (76, 3.75, 0.375),  # D7
    # Bar 4
    (64, 4.5, 0.375), (67, 4.5, 0.375), (72, 4.5, 0.375), (76, 4.5, 0.375),  # D7
    (64, 5.25, 0.375), (67, 5.25, 0.375), (72, 5.25, 0.375), (76, 5.25, 0.375)   # D7
]
for note, start, duration in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(p)

# Sax - melody in D, short motif, starts on beat 1 of bar 2
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (67, 2.25, 0.375), (64, 2.625, 0.375),  # First motif
    (62, 3.0, 0.375), (64, 3.375, 0.375), (67, 3.75, 0.375), (64, 4.125, 0.375),  # Repeat motif
    (62, 4.5, 0.375), (64, 4.875, 0.375), (67, 5.25, 0.375), (64, 5.625, 0.375)   # Final repetition
]
for note, start, duration in sax_notes:
    s = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(s)

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
