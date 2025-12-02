
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

# Marcus: Walking bass line in Fm
bass_notes = [
    (20, 1.5), (19, 1.875), (21, 2.25), (20, 2.625),
    (20, 3.0), (19, 3.375), (21, 3.75), (20, 4.125),
    (20, 4.5), (19, 4.875), (21, 5.25), (20, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    (39, 2.625), (44, 2.625), (46, 2.625), (50, 2.625),
    # Bar 3: Bb7 on 2 and 4
    (45, 4.125), (49, 4.125), (51, 4.125), (53, 4.125),
    # Bar 4: Eb7 on 2 and 4
    (41, 5.625), (45, 5.625), (47, 5.625), (51, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.1875))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax melody
# One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start the motif
    (42, 1.5), (44, 1.875), (42, 2.25),
    # Bar 3: Repeat the first two notes
    (42, 3.0), (44, 3.375),
    # Bar 4: Finish the motif with a resolution
    (40, 4.5), (42, 4.875), (40, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
