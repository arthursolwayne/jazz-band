
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Saxophone
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=80, pitch=drum_notes['kick'], start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=80, pitch=drum_notes['snare'], start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=70, pitch=drum_notes['hihat'], start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    (1.5, 62),   # D3
    (1.875, 63), # Eb3
    (2.25, 64),  # E3
    (2.625, 62), # D3
    (2.875, 60), # C3
    (3.25, 62),  # D3
    (3.625, 63), # Eb3
    (4.0, 64),   # E3
    (4.375, 62), # D3
    (4.75, 60),  # C3
    (5.125, 62), # D3
    (5.5, 63),   # Eb3
    (5.875, 64), # E3
    (6.25, 62)   # D3
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    (1.875, 62),  # D3 (Dm7: D, F, A, C)
    (1.875, 64),  # F3
    (1.875, 67),  # A3
    (1.875, 69),  # C4
    (2.625, 62),  # D3
    (2.625, 64),  # F3
    (2.625, 67),  # A3
    (2.625, 69),  # C4
    (4.375, 62),  # D3
    (4.375, 64),  # F3
    (4.375, 67),  # A3
    (4.375, 69),  # C4
    (5.125, 62),  # D3
    (5.125, 64),  # F3
    (5.125, 67),  # A3
    (5.125, 69)   # C4
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Dante, motif - short, singing, leaving it hanging
sax_notes = [
    (1.5, 65),  # E4
    (1.75, 67), # G4
    (2.0, 64),  # F4
    (2.25, 65), # E4
    (2.5, 67),  # G4
    (2.75, 64), # F4
    (3.0, 62),  # D4
    (3.25, 64), # F4
    (3.5, 65),  # E4
    (3.75, 67), # G4
    (4.0, 64),  # F4
    (4.25, 62), # D4
    (4.5, 64),  # F4
    (4.75, 65), # E4
    (5.0, 67),  # G4
    (5.25, 64), # F4
    (5.5, 62),  # D4
    (5.75, 64), # F4
    (6.0, 65)   # E4
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
