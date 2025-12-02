
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (walking, chromatic approaches)
bass_notes = [
    (37, 1.5), (39, 1.875), (40, 2.25), (42, 2.625),
    (43, 3.0), (41, 3.375), (39, 3.75), (37, 4.125),
    (38, 4.5), (40, 4.875), (42, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (57, 1.5), (60, 1.5), (64, 1.5), (67, 1.5),  # F7
    (57, 2.25), (60, 2.25), (64, 2.25), (67, 2.25),  # F7
    # Bar 3 (3.0 - 4.5s)
    (59, 3.0), (62, 3.0), (66, 3.0), (69, 3.0),  # Bb7
    (59, 3.75), (62, 3.75), (66, 3.75), (69, 3.75),  # Bb7
    # Bar 4 (4.5 - 6.0s)
    (57, 4.5), (60, 4.5), (64, 4.5), (67, 4.5),  # F7
    (57, 5.25), (60, 5.25), (64, 5.25), (67, 5.25)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Saxophone motif (start it, leave it hanging, come back and finish it)
# F (57), G (58), Bb (60), F (57)
sax_notes = [
    (57, 1.5), (58, 1.75), (60, 2.0), (57, 2.25),
    (57, 4.5), (58, 4.75), (60, 5.0), (57, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
