
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4 (1.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (61, 2.25, 0.375), (60, 2.625, 0.375),
    (62, 3.0, 0.375), (63, 3.375, 0.375), (61, 3.75, 0.375), (60, 4.125, 0.375),
    (62, 4.5, 0.375), (63, 4.875, 0.375), (61, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.875, 0.125), (67, 1.875, 0.125), (71, 1.875, 0.125), (72, 1.875, 0.125),
    # Bar 3
    (64, 3.375, 0.125), (67, 3.375, 0.125), (71, 3.375, 0.125), (72, 3.375, 0.125),
    # Bar 4
    (64, 4.875, 0.125), (67, 4.875, 0.125), (71, 4.875, 0.125), (72, 4.875, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (42, 1.5, 0.125),
    (38, 1.875, 0.375), (42, 1.875, 0.125),
    (36, 2.25, 0.375), (42, 2.25, 0.125),
    (38, 2.625, 0.375), (42, 2.625, 0.125),
    (36, 3.0, 0.375), (42, 3.0, 0.125),
    (38, 3.375, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (42, 3.75, 0.125),
    (38, 4.125, 0.375), (42, 4.125, 0.125),
    (36, 4.5, 0.375), (42, 4.5, 0.125),
    (38, 4.875, 0.375), (42, 4.875, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    (62, 1.5, 0.25),  # D
    (64, 1.75, 0.25),  # E
    # Bar 3: Silence, then return
    (62, 3.0, 0.25),  # D
    (64, 3.25, 0.25),  # E
    # Bar 4: End with a question
    (62, 4.5, 0.25),  # D
    (64, 4.75, 0.25)   # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
