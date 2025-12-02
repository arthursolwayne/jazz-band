
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize a Pretty MIDI object with 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time and note values
bar_length = 1.5  # in seconds
beat_length = 0.375  # 160 BPM = 60/160 = 0.375s per beat
time = 0.0

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
bass = Instrument(program=Program.FROM_PROGRAM(33))
sax = Instrument(program=Program.TENOR_SAX)

pm.instruments.append(drums)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(sax)

# ======================
# 1. DRUMS: Little Ray
# ======================
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(time):
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = Note(velocity=100, pitch=36, start=time + beat * beat_length, end=time + beat * beat_length + 0.1)
        drums.notes.append(note)
    
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = Note(velocity=90, pitch=38, start=time + beat * beat_length, end=time + beat * beat_length + 0.1)
        drums.notes.append(note)
    
    # Hihat on every eighth
    for eighth in range(8):
        note = Note(velocity=80, pitch=42, start=time + eighth * beat_length / 2, end=time + eighth * beat_length / 2 + 0.05)
        drums.notes.append(note)

# Bar 1
add_drums(time)

time += bar_length

# ======================
# 2. PIANO: Diane (Bars 2-4)
# ======================
# Comping on 2 and 4 with 7th chords
# Fm7 = F, Ab, C, Eb
# Bbm7 = Bb, Db, F, Ab
# Cm7 = C, Eb, G, Bb
# Gm7 = G, Bb, D, F

def add_piano(time):
    # Bar 2: Fm7 comp on beat 2
    for note in [53, 55, 57, 59]:  # F, Ab, C, Eb
        n = Note(velocity=80, pitch=note, start=time + 1 * beat_length, end=time + 1 * beat_length + 0.3)
        piano.notes.append(n)
    
    # Bar 3: Bbm7 comp on beat 2
    for note in [52, 54, 56, 58]:  # Bb, Db, F, Ab
        n = Note(velocity=80, pitch=note, start=time + 2 * beat_length, end=time + 2 * beat_length + 0.3)
        piano.notes.append(n)
    
    # Bar 4: Cm7 comp on beat 2
    for note in [55, 57, 59, 61]:  # C, Eb, G, Bb
        n = Note(velocity=80, pitch=note, start=time + 3 * beat_length, end=time + 3 * beat_length + 0.3)
        piano.notes.append(n)

add_piano(time)

# ======================
# 3. BASS: Marcus (Bars 2-4)
# ======================
# Walking line, chromatic approaches, no repeated notes
# Fm -> Bb -> C -> Eb -> F

def add_bass(time):
    # Bar 2: Fm
    # F -> Gb (chromatic) -> G -> A (chromatic) -> Bb
    notes = [53, 54, 55, 56, 57]
    for i, note in enumerate(notes):
        n = Note(velocity=80, pitch=note, start=time + i * beat_length, end=time + i * beat_length + 0.25)
        bass.notes.append(n)
    
    # Bar 3: Bbm
    # Bb -> C (chromatic) -> C# -> D (chromatic) -> Eb
    notes = [52, 55, 56, 57, 59]
    for i, note in enumerate(notes):
        n = Note(velocity=80, pitch=note, start=time + 4 * beat_length + i * beat_length, end=time + 4 * beat_length + i * beat_length + 0.25)
        bass.notes.append(n)
    
    # Bar 4: Cm
    # C -> Db (chromatic) -> D -> Eb (chromatic) -> F
    notes = [55, 56, 57, 59, 60]
    for i, note in enumerate(notes):
        n = Note(velocity=80, pitch=note, start=time + 8 * beat_length + i * beat_length, end=time + 8 * beat_length + i * beat_length + 0.25)
        bass.notes.append(n)

add_bass(time)

# ======================
# 4. SAX: Dante (Bars 2-4)
# ======================
# Motif: F -> Gb -> G -> F (hanging) -> Return on bar 4 with F -> Gb -> Ab -> F
# Start it, leave it hanging, come back and finish it.

def add_sax(time):
    # Bar 2: F -> Gb -> G -> F (hang on F)
    notes = [53, 54, 55, 53]
    for i, note in enumerate(notes):
        n = Note(velocity=100, pitch=note, start=time + i * beat_length, end=time + i * beat_length + 0.5)
        sax.notes.append(n)
    
    # Bar 3: Rest
    # Just silence
    
    # Bar 4: Return with motif, now F -> Gb -> Ab -> F
    notes = [53, 54, 56, 53]
    for i, note in enumerate(notes):
        n = Note(velocity=100, pitch=note, start=time + 6 * beat_length + i * beat_length, end=time + 6 * beat_length + i * beat_length + 0.5)
        sax.notes.append(n)

add_sax(time)

# Save the MIDI file
pm.write('waynes_intro.mid')
print("MIDI file written as 'waynes_intro.mid'")
