
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (61, 2.25), (60, 2.625),
    (62, 3.0), (63, 3.375), (61, 3.75), (60, 4.125),
    (62, 4.5), (63, 4.875), (61, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5-3.0s)
    (62, 1.875), (67, 1.875), (69, 1.875), (71, 1.875),  # D7
    (62, 3.0), (67, 3.0), (69, 3.0), (71, 3.0),  # D7
    # Bar 3 (3.0-4.5s)
    (62, 3.375), (67, 3.375), (69, 3.375), (71, 3.375),  # D7
    (62, 4.5), (67, 4.5), (69, 4.5), (71, 4.5),  # D7
    # Bar 4 (4.5-6.0s)
    (62, 4.875), (67, 4.875), (69, 4.875), (71, 4.875),  # D7
    (62, 6.0), (67, 6.0), (69, 6.0), (71, 6.0)  # D7
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax (Dante): Motif in Dm
# Start with D (62), F (65), G (67), Bb (69) => Dm7
# Repeat with a chromatic approach: C# (63), D (62), F (65), G (67)
sax_notes = [
    (62, 1.5), (65, 1.5), (67, 1.5), (69, 1.5),
    (63, 2.25), (62, 2.25), (65, 2.25), (67, 2.25),
    (62, 3.0), (65, 3.0), (67, 3.0), (69, 3.0),
    (63, 3.75), (62, 3.75), (65, 3.75), (67, 3.75),
    (62, 4.5), (65, 4.5), (67, 4.5), (69, 4.5),
    (63, 5.25), (62, 5.25), (65, 5.25), (67, 5.25)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(n)

# Drums: Fill the bar
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    # Bar 3
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
