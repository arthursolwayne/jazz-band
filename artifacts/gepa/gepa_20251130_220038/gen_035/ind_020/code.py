
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
    (0.0, 36, 100), (0.375, 42, 100),
    (0.75, 38, 100), (1.125, 42, 100),
    (1.5, 36, 100), (1.875, 42, 100),
    (2.25, 38, 100), (2.625, 42, 100)
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bars 2-4 (1.5 - 6.0s)

# Marcus: Walking bass line in D (D F# A B) with chromatic approaches
bass_notes = [
    (1.5, 65, 100), (1.875, 67, 100), (2.25, 69, 100), (2.625, 71, 100),
    (3.0, 67, 100), (3.375, 65, 100), (3.75, 64, 100), (4.125, 65, 100),
    (4.5, 67, 100), (4.875, 69, 100), (5.25, 71, 100), (5.625, 69, 100)
]
for time, note, velocity in bass_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4 in D (D7, G7, A7, D7)
piano_notes = [
    # Bar 2 (1.5 - 2.25s) - D7
    (1.5, 67, 100), (1.5, 69, 100), (1.5, 72, 100), (1.5, 74, 100),
    # Bar 3 (2.625 - 3.375s) - G7
    (2.625, 71, 100), (2.625, 74, 100), (2.625, 76, 100), (2.625, 79, 100),
    # Bar 4 (4.125 - 4.875s) - A7
    (4.125, 72, 100), (4.125, 74, 100), (4.125, 76, 100), (4.125, 79, 100),
    # Bar 4 (5.25 - 6.0s) - D7
    (5.25, 67, 100), (5.25, 69, 100), (5.25, 72, 100), (5.25, 74, 100)
]
for time, note, velocity in piano_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note_obj)

# Dante: Sax solo (bars 2-4)
# Whisper at first, then cry. One motif, with rests and space.

sax_notes = [
    # Bar 2 (1.5 - 2.25s)
    (1.5, 72, 90),     # D
    (1.75, 76, 90),    # G
    (2.0, 74, 90),     # F#
    (2.125, 72, 90),   # D (end of bar)
    
    # Bar 3 (2.25 - 3.0s)
    (2.25, 76, 100),   # G
    (2.5, 74, 100),    # F#
    (2.75, 72, 100),   # D
    (3.0, 76, 100),    # G
    
    # Bar 4 (3.0 - 3.75s)
    (3.0, 72, 100),    # D
    (3.25, 76, 100),   # G
    (3.5, 79, 100),    # B
    (3.75, 82, 100),   # D (octave)
    
    # Bar 4 (3.75 - 4.5s)
    (3.75, 79, 90),    # B
    (4.0, 76, 90),     # G
    (4.25, 72, 90),    # D
    (4.5, 79, 90),     # B
    
    # Bar 4 (4.5 - 5.25s)
    (4.5, 76, 100),    # G
    (4.75, 79, 100),   # B
    (5.0, 82, 100),    # D (octave)
    (5.25, 82, 100)    # D (octave)
]
for time, note, velocity in sax_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
