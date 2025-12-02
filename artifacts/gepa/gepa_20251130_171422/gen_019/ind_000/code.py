
import pretty_midi

# Initialize the MIDI file with tempo 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone
bass = pretty_midi.Instrument(program=33)      # Acoustic bass
piano = pretty_midi.Instrument(program=0)      # Electric piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds
for bar in range(1):
    for beat in [0, 1, 2, 3]:
        time = bar * bar_length + beat * (bar_length / 4)
        if beat in [0, 2]:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat in [1, 3]:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-hat on every eighth note
        for eighth in [0, 1]:
            hihat_time = time + eighth * (bar_length / 8)
            hihat_note = pretty_midi.Note(velocity=70, pitch=drum_notes['hihat'], start=hihat_time, end=hihat_time + 0.05)
            drums.notes.append(hihat_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.25),  # D3
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=1.75 + 0.25), # Eb3
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.0 + 0.25),   # E3
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.25 + 0.25), # F3
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.5 + 0.25),   # G3
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=2.75 + 0.25), # A3
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.0 + 0.25),   # Bb3
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.25 + 0.25), # B3
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.5 + 0.25),   # C4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.75 + 0.25), # B3
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.0 + 0.25),   # Bb3
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.25 + 0.25), # A3
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.5 + 0.25),   # G3
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=4.75 + 0.25), # F3
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.0 + 0.25),   # E3
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.25 + 0.25), # Eb3
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
# Dm7: D F A C
# Chords every two beats (on 2 and 4)
# Time = 1.5 - 3.0, 3.0 - 4.5, 4.5 - 6.0

def add_piano_chord(start_time, chord, duration=0.5):
    for note in chord:
        pretty_midi.Note(velocity=95, pitch=note, start=start_time, end=start_time + duration, instrument=piano)

# Dm7 chord
dm7 = [62, 65, 67, 70]  # D (D3), F (F3), A (A3), C (C4)

# Chord on beat 2 of bar 2 (time = 1.75)
# Chord on beat 4 of bar 2 (time = 2.25)
# Chord on beat 2 of bar 3 (time = 3.25)
# Chord on beat 4 of bar 3 (time = 3.75)
# Chord on beat 2 of bar 4 (time = 4.75)
# Chord on beat 4 of bar 4 (time = 5.25)

add_piano_chord(1.75, dm7)
add_piano_chord(2.25, dm7)
add_piano_chord(3.25, dm7)
add_piano_chord(3.75, dm7)
add_piano_chord(4.75, dm7)
add_piano_chord(5.25, dm7)

# Saxophone: Dante - short motif, make it sing.
# Motif: D (62), F# (66), B (71), D (62) — a Dm7 arpeggio with a chromatic approach to F#
# Play on beat 1 of bar 2 (time = 1.5)
# Let it hang on beat 2 (time = 1.75), then come back and finish it on beat 3 (time = 2.0)

# First note: D (62)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
sax.notes.append(note)

# Second note: F# (66)
note = pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25)
sax.notes.append(note)

# Third note: B (71)
note = pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5)
sax.notes.append(note)

# Final note: D (62)
note = pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75)
sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in [0, 1, 2, 3]:
        time = bar * bar_length + beat * (bar_length / 4)
        if beat in [0, 2]:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat in [1, 3]:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-hat on every eighth note
        for eighth in [0, 1]:
            hihat_time = time + eighth * (bar_length / 8)
            hihat_note = pretty_midi.Note(velocity=70, pitch=drum_notes['hihat'], start=hihat_time, end=hihat_time + 0.05)
            drums.notes.append(hihat_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
