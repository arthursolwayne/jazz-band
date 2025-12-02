
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

def add_note(instrument, pitch, start, end, velocity=100):
    note = pretty_midi.Note(velocity, pitch, start, end)
    instrument.notes.append(note)

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3
add_note(drums, drum_notes['kick'], 0.0, 0.375)
add_note(drums, drum_notes['kick'], 1.125, 1.5)

# Snare on 2 and 4
add_note(drums, drum_notes['snare'], 0.75, 1.125)
add_note(drums, drum_notes['snare'], 1.875, 2.25)

# Hi-hat on every eighth note
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for t in hihat_times:
    add_note(drums, drum_notes['hihat'], t, t + 0.125, velocity=80)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm
# Dm: D, F, A, C
# Walking bass line: D -> F -> A -> C -> D -> F -> A -> C
bass_notes = [62, 65, 67, 69, 62, 65, 67, 69]
bass_times = [1.5 + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    add_note(bass, note, time, time + 0.375, velocity=80)

# Piano: 7th chords on 2 and 4
# Dm7 = D F A C
# Gm7 = G Bb D F
# Cm7 = C Eb G Bb
# Fm7 = F Ab C Eb

# Bar 2: 2nd beat = Gm7, 4th beat = Cm7
add_note(piano, 67, 2.25, 2.625)  # G
add_note(piano, 71, 2.25, 2.625)  # Bb
add_note(piano, 62, 2.25, 2.625)  # D
add_note(piano, 65, 2.25, 2.625)  # F

add_note(piano, 60, 3.0, 3.375)  # C
add_note(piano, 64, 3.0, 3.375)  # Eb
add_note(piano, 67, 3.0, 3.375)  # G
add_note(piano, 71, 3.0, 3.375)  # Bb

# Sax: Motif in D minor
# Simple, singable, melodic phrase (D, F, A, Bb -> D, F, G, A)

# Bar 2: 1st beat
add_note(sax, 62, 1.5, 1.875, velocity=100)  # D
add_note(sax, 65, 1.875, 2.25, velocity=100)  # F
add_note(sax, 67, 2.25, 2.625, velocity=100)  # A
add_note(sax, 68, 2.625, 3.0, velocity=100)   # Bb

# Bar 3: 1st beat (fragment, leave it hanging)
add_note(sax, 62, 3.0, 3.375, velocity=100)  # D
add_note(sax, 65, 3.375, 3.75, velocity=100)  # F
add_note(sax, 67, 3.75, 4.125, velocity=100)  # A
add_note(sax, 68, 4.125, 4.5, velocity=100)   # Bb

# Bar 4: 1st beat (complete the motif)
add_note(sax, 62, 4.5, 4.875, velocity=100)  # D
add_note(sax, 65, 4.875, 5.25, velocity=100)  # F
add_note(sax, 67, 5.25, 5.625, velocity=100)  # A
add_note(sax, 68, 5.625, 6.0, velocity=100)   # Bb

# Piano: Bar 3 and 4 comp (same as bar 2)
# Bar 3: 2nd beat = Fm7, 4th beat = Dm7
add_note(piano, 65, 3.75, 4.125)  # F
add_note(piano, 68, 3.75, 4.125)  # Ab
add_note(piano, 62, 3.75, 4.125)  # C
add_note(piano, 65, 3.75, 4.125)  # Eb

add_note(piano, 62, 4.5, 4.875)  # D
add_note(piano, 65, 4.5, 4.875)  # F
add_note(piano, 67, 4.5, 4.875)  # A
add_note(piano, 69, 4.5, 4.875)  # C

# Bar 4: 2nd beat = Gm7, 4th beat = Cm7 (same as bar 2)
add_note(piano, 67, 5.25, 5.625)  # G
add_note(piano, 71, 5.25, 5.625)  # Bb
add_note(piano, 62, 5.25, 5.625)  # D
add_note(piano, 65, 5.25, 5.625)  # F

add_note(piano, 60, 6.0, 6.375)  # C
add_note(piano, 64, 6.0, 6.375)  # Eb
add_note(piano, 67, 6.0, 6.375)  # G
add_note(piano, 71, 6.0, 6.375)  # Bb

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
