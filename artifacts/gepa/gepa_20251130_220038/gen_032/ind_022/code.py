
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
    (36, 2.25), (38, 2.625), (42, 2.625),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 3.0), (46, 3.375), (44, 3.75), (43, 4.125),
    (45, 4.5), (46, 4.875), (44, 5.25), (43, 5.625),
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (57, 3.0), (60, 3.0), (64, 3.0), (62, 3.0),  # C7 at beat 2
    (57, 4.5), (60, 4.5), (64, 4.5), (62, 4.5),  # C7 at beat 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5, 0.5),  # Start motif on beat 1
    (65, 2.0, 0.25), # Leave it hanging
    (62, 3.0, 0.5),  # Come back
    (65, 3.5, 0.25), # End with a question
    (67, 4.0, 0.5),  # Resolve it
    (62, 4.5, 0.5),  # Return to the start
]
for note, time, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
