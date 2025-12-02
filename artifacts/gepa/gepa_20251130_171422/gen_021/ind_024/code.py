
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drums_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts, leaves it hanging
sax_notes = [
    (60, 1.5), (62, 1.75), (64, 2.0), (62, 2.25), (60, 2.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bass: walking line with chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.75), (50, 2.0), (51, 2.25),
    (52, 2.5), (51, 2.75), (50, 3.0), (49, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.75), (67, 1.75), (69, 1.75), (71, 1.75), # C7 on 2
    (64, 2.75), (67, 2.75), (69, 2.75), (71, 2.75)  # C7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 3: Sax continues motif, tension builds
sax_notes = [
    (60, 3.0), (62, 3.25), (64, 3.5), (62, 3.75), (60, 4.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bass: walking line with chromatic approaches
bass_notes = [
    (52, 3.0), (51, 3.25), (50, 3.5), (49, 3.75),
    (48, 4.0), (49, 4.25), (50, 4.5), (51, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.25), (67, 3.25), (69, 3.25), (71, 3.25), # C7 on 2
    (64, 4.25), (67, 4.25), (69, 4.25), (71, 4.25)  # C7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drums_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Sax finishes the motif, piano resolves
sax_notes = [
    (60, 4.5), (62, 4.75), (64, 5.0), (62, 5.25), (60, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bass: walking line with chromatic approaches
bass_notes = [
    (51, 4.5), (50, 4.75), (49, 5.0), (48, 5.25),
    (49, 5.5), (50, 5.75), (51, 6.0), (52, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 4.75), (67, 4.75), (69, 4.75), (71, 4.75), # C7 on 2
    (64, 5.75), (67, 5.75), (69, 5.75), (71, 5.75)  # C7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drums_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
