
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

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (62, 2.625),  # Dm7
    (64, 3.0), (65, 3.375), (62, 3.75), (64, 4.125),  # G7
    (67, 4.5), (68, 4.875), (65, 5.25), (67, 5.625)   # Cm7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 2.25), (67, 2.25), (69, 2.25), (71, 2.25),  # Dm7
    # Bar 3
    (64, 3.375), (69, 3.375), (71, 3.375), (72, 3.375),  # G7
    # Bar 4
    (67, 4.875), (72, 4.875), (74, 4.875), (76, 4.875)   # Cm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums (Little Ray): kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in range(2, 5):
    for beat in range(4):
        time = 1.5 + (bar - 2) * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        elif beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Sax (Dante): motif starts at 1.5s
# Motif: Dm (62), F (65), G (67), D (62)
# Start: 1.5s, then repeat at 2.625s, then resolve at 4.125s
sax_notes = [
    (62, 1.5), (65, 1.875), (67, 2.25), (62, 2.625),
    (62, 2.625), (65, 2.875), (67, 3.125), (62, 3.5),
    (62, 4.125), (65, 4.375), (67, 4.625), (62, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
