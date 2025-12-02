
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

# Bass line - walking line, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 2.875), (46, 3.25), (44, 3.625), (43, 4.0),
    (45, 4.375), (46, 4.75), (44, 5.125), (43, 5.5)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (64, 2.25), (67, 2.25), (69, 2.25), (71, 2.25),
    # Bar 3: Bb7 on beat 2
    (67, 3.25), (70, 3.25), (72, 3.25), (74, 3.25),
    # Bar 4: D7 on beat 2
    (69, 4.25), (71, 4.25), (73, 4.25), (76, 4.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax - motif: F (64) -> Ab (66) -> Bb (67) -> D (69), then leave it hanging
sax_notes = [
    (64, 1.5), (66, 1.875), (67, 2.25), (69, 2.625),
    (69, 2.625)  # Hold the last note
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
