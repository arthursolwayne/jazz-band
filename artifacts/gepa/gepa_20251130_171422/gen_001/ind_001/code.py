
import pretty_midi

# Constants
TEMPO = 160  # BPM
TIME_SIGNATURE = (4, 4)
DURATION = 6.0  # seconds
NOTE_DURATION = 0.375  # 1/16 note in seconds (60 / 160 = 0.375)

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Bass
piano = pretty_midi.Instrument(program=0)   # Piano
sax = pretty_midi.Instrument(program=64)    # Tenor Sax

pm.instruments = [drums, bass, piano, sax]

# Bar 1: Drums - Driving, syncopated rhythm
def add_drums():
    # Hi-Hat on every eighth note (0.375s)
    for i in range(16):
        note = pretty_midi.Note(velocity=80, pitch=42, start=i * NOTE_DURATION, end=(i + 1) * NOTE_DURATION)
        drums.notes.append(note)
    
    # Kick on 1 and 3 (beats 0 and 2)
    for i in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=i * NOTE_DURATION * 4, end=(i + 1) * NOTE_DURATION * 4)
        drums.notes.append(note)
    
    # Snare on 2 and 4 (beats 1 and 3)
    for i in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=i * NOTE_DURATION * 4, end=(i + 1) * NOTE_DURATION * 4)
        drums.notes.append(note)

# Bar 2–4: Sax motif (Dm7, Dm, D7)
def add_sax():
    # Dm7: D, F, A, C
    # Motif: D -> F -> A -> C -> B -> A -> G -> A -> (hanging)
    # Starting on beat 2 of bar 2 (0.75s)
    note = pretty_midi.Note(velocity=100, pitch=62, start=0.75, end=0.75 + NOTE_DURATION)
    sax.notes.append(note)

    note = pretty_midi.Note(velocity=100, pitch=65, start=1.125, end=1.125 + NOTE_DURATION)
    sax.notes.append(note)

    note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + NOTE_DURATION)
    sax.notes.append(note)

    note = pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=1.875 + NOTE_DURATION)
    sax.notes.append(note)

    # Chromatic descent: B -> A -> G -> A (hanging)
    note = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.25 + NOTE_DURATION)
    sax.notes.append(note)

    note = pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.625 + NOTE_DURATION)
    sax.notes.append(note)

    note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + NOTE_DURATION)
    sax.notes.append(note)

    note = pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.375 + NOTE_DURATION)
    sax.notes.append(note)

# Bass: Walking line, chromatic, Dm7 -> D7 -> G7 -> C7
def add_bass():
    # Dm7: D, F, A, C
    # Chromatic walking line
    notes = [62, 63, 65, 64, 67, 68, 70, 69, 67, 65, 64, 62, 63, 64, 66, 67, 70, 69, 71, 70, 69, 67, 64, 65]
    for i, pitch in enumerate(notes):
        start = i * NOTE_DURATION
        end = start + NOTE_DURATION
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4, with tension
def add_piano():
    # Dm7: D, F, A, C
    # D7: D, F#, A, C
    # G7: G, B, D, F
    # C7: C, E, G, B

    # Bar 2: Dm7 (comp on beat 2)
    note = pretty_midi.Note(velocity=90, pitch=62, start=1.125, end=1.125 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=65, start=1.125, end=1.125 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=67, start=1.125, end=1.125 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=69, start=1.125, end=1.125 + NOTE_DURATION)
    piano.notes.append(note)

    # Bar 3: D7 (comp on beat 2)
    note = pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.625 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.625 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.625 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.625 + NOTE_DURATION)
    piano.notes.append(note)

    # Bar 4: G7 (comp on beat 2)
    note = pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.125 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.125 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.125 + NOTE_DURATION)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.125 + NOTE_DURATION)
    piano.notes.append(note)

# Add everything
add_drums()
add_sax()
add_bass()
add_piano()

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file created: 'dante_intro.mid'")
