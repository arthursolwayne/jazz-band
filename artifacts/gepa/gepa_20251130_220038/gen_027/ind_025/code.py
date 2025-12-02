
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (43, 2.25),
    (45, 2.5), (46, 2.75), (44, 3.0), (43, 3.25),
    (45, 3.5), (46, 3.75), (44, 4.0), (43, 4.25),
    (45, 4.5), (46, 4.75), (44, 5.0), (43, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2, Bb7 on beat 4
    (59, 2.0), (61, 2.0), (62, 2.0), (64, 2.0),
    (57, 4.0), (59, 4.0), (60, 4.0), (62, 4.0),
    # Bar 3: Bb7 on beat 2, Eb7 on beat 4
    (61, 5.0), (63, 5.0), (64, 5.0), (66, 5.0),
    (58, 7.0), (60, 7.0), (61, 7.0), (63, 7.0),
    # Bar 4: Eb7 on beat 2, Ab7 on beat 4
    (63, 8.0), (65, 8.0), (66, 8.0), (68, 8.0),
    (59, 10.0), (61, 10.0), (62, 10.0), (64, 10.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G#, A, F (motif)
sax_notes = [
    (59, 1.5), (61, 1.75), (62, 2.0), (59, 2.25),  # First phrase
    (59, 3.5), (61, 3.75), (62, 4.0), (59, 4.25)   # Second phrase
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
