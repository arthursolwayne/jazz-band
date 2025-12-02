
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

# Bass line: Walking line in Fm, chromatic approaches, never the same note twice
bass_notes = [
    (42, 1.5), (43, 1.75), (40, 2.0), (38, 2.25),
    (42, 2.5), (43, 2.75), (40, 3.0), (38, 3.25),
    (42, 3.5), (43, 3.75), (40, 4.0), (38, 4.25),
    (42, 4.5), (43, 4.75), (40, 5.0), (38, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    (44, 2.0), (40, 2.0), (41, 2.0), (43, 2.0),
    (44, 2.5), (40, 2.5), (41, 2.5), (43, 2.5),
    # Bar 3: Bbm7 on 2 and 4
    (41, 3.0), (37, 3.0), (38, 3.0), (40, 3.0),
    (41, 3.5), (37, 3.5), (38, 3.5), (40, 3.5),
    # Bar 4: Ebm7 on 2 and 4
    (39, 4.0), (35, 4.0), (36, 4.0), (38, 4.0),
    (39, 4.5), (35, 4.5), (36, 4.5), (38, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, E
sax_notes = [
    (44, 1.5), (41, 1.75), (42, 2.0), (47, 2.25),  # Start the motif
    (44, 2.5), (41, 2.75), (42, 3.0), (47, 3.25),  # Repeat the motif
    (44, 3.5), (41, 3.75), (42, 4.0), (47, 4.25),  # Repeat the motif
    (44, 4.5), (41, 4.75), (42, 5.0), (47, 5.25)   # Repeat the motif
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.125)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.375 + 0.125)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.125)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.375 + 0.125)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 0.75 + 0.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.125 + 0.125)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
