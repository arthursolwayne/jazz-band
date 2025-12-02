
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
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - walking line in Fm, chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.875), (47, 2.25), (46, 2.625),
    (48, 3.0), (49, 3.375), (47, 3.75), (46, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (50, 1.875), (53, 1.875), (60, 1.875), (62, 1.875),
    # Bar 3: Ab7 on beat 2
    (57, 3.375), (60, 3.375), (65, 3.375), (67, 3.375),
    # Bar 4: Dm7 on beat 2
    (57, 4.875), (60, 4.875), (62, 4.875), (64, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax - motif: F, Ab, Bb, F (start on beat 1)
sax_notes = [
    (50, 1.5), (53, 1.875), (57, 2.25), (50, 2.625),
    # Leave it hanging
    (53, 3.0), (57, 3.375), (60, 3.75), (50, 4.125),
    # Come back
    (53, 4.5), (57, 4.875), (60, 5.25), (50, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.875))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.495))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.245))
    # Hi-hat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
