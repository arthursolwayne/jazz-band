
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
    (36, 0.0), (38, 0.375), (42, 0.375), (36, 0.75),
    (38, 1.125), (42, 1.125), (36, 1.5)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (65, 2.625),
    (67, 3.0)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    (67, 2.0), (71, 2.0), (69, 2.0), (72, 2.0),
    # Bar 3: Bm7 on beat 2
    (71, 3.5), (74, 3.5), (72, 3.5), (75, 3.5),
    # Bar 4: F#7 on beat 2
    (76, 5.0), (80, 5.0), (78, 5.0), (81, 5.0)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Motif starting at 1.5s
sax_notes = [
    # Bar 2: Start of the motif
    (67, 1.5), (69, 1.75), (67, 2.0),
    # Bar 3: Leave it hanging
    (69, 3.0),
    # Bar 4: Return and finish
    (67, 4.5), (69, 4.75), (67, 5.0)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 2: Drums continue
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (36, 2.25),
    (38, 2.625), (42, 2.625), (36, 3.0)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 3: Drums continue
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375), (36, 3.75),
    (38, 4.125), (42, 4.125), (36, 4.5)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4: Drums continue
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875), (36, 5.25),
    (38, 5.625), (42, 5.625), (36, 6.0)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
