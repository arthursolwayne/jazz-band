
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (61, 1.5), (62, 1.75), (60, 2.0), (59, 2.25),
    (57, 2.5), (58, 2.75), (56, 3.0), (55, 3.25),
    (54, 3.5), (53, 3.75), (52, 4.0), (51, 4.25),
    (50, 4.5), (49, 4.75), (48, 5.0), (47, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 2.0), (64, 2.0), (67, 2.0), (70, 2.0),  # Dm7
    (62, 3.0), (66, 3.0), (69, 3.0), (72, 3.0),  # F7
    (64, 4.0), (68, 4.0), (71, 4.0), (74, 4.0),  # A7
    (65, 5.0), (69, 5.0), (72, 5.0), (75, 5.0)   # C7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.75), (65, 2.0),  # First phrase
    (64, 2.5), (62, 2.75), (60, 3.0),  # Second phrase
    (62, 3.5), (64, 3.75), (65, 4.0),  # Third phrase
    (64, 4.5), (62, 4.75), (60, 5.0)   # Final phrase
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
