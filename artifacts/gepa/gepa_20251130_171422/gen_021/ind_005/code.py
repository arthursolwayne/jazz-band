
import pretty_midi
from pretty_midi import Note, Instrument, TimeSignature, KeySignature

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
pm.time_signature_changes = [TimeSignature(numerator=4, denominator=4, time=0)]
pm.key_signature_changes = [KeySignature(key_number=21, time=0)]  # F minor

# Define the tempo
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Helper function to convert note name to MIDI note number
def note_to_midi(note_name):
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1,
        'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6,
        'G': 7, 'G#': 8, 'Ab': 8,
        'A': 9, 'A#': 10, 'Bb': 10,
        'B': 11
    }
    note, accidental = note_name[0], note_name[1:] if len(note_name) > 1 else ''
    base = note_map[note]
    if accidental == '#':
        base += 1
    elif accidental == 'b':
        base -= 1
    return base + 60  # MIDI note number for C4 (60) as reference

# Define the root and scale
root = 'F'
scale = ['F', 'Ab', 'Bb', 'B', 'C', 'Db', 'Eb']  # F minor (harmonic)

# Create instruments
drums = Instrument(program=12, is_drum=True)
piano = Instrument(program=0)
bass = Instrument(program=33)
sax = Instrument(program=64)

# Define timing (6 seconds for 4 bars at 160 BPM)
bar_length = 1.5  # seconds per bar
time = 0.0

# --- Bar 1: Little Ray (Drums) - Groove only ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [note_to_midi('C1')]  # C1 = MIDI 36
snare_notes = [note_to_midi('C2')]  # C2 = MIDI 60
hihat_notes = [note_to_midi('C4')]  # C4 = MIDI 60

# Kick on 1 and 3
kick_times = [0.0, 0.75]
for t in kick_times:
    note = Note(velocity=100, start=t, end=t + 0.25)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [0.5, 1.25]
for t in snare_times:
    note = Note(velocity=100, start=t, end=t + 0.25)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [0.0, 0.375, 0.75, 1.125]
for t in hihat_times:
    note = Note(velocity=90, start=t, end=t + 0.125)
    drums.notes.append(note)

pm.instruments.append(drums)

# --- Bar 2: Bass, Piano, Sax join in (Bars 2-4) ---
# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    note_to_midi('F'),       # 0.0
    note_to_midi('Gb'),      # 0.375
    note_to_midi('F'),       # 0.75
    note_to_midi('Eb'),      # 1.125
    note_to_midi('D'),       # 1.5
    note_to_midi('Eb'),      # 1.875
    note_to_midi('F'),       # 2.25
    note_to_midi('G'),       # 2.625
]
bass_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for t, pitch in zip(bass_times, bass_notes):
    note = Note(velocity=85, start=t, end=t + 0.25)
    bass.notes.append(note)

pm.instruments.append(bass)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    note_to_midi('F'),       # F7 = F, A, C, Eb
    note_to_midi('A'),
    note_to_midi('C'),
    note_to_midi('Eb'),
    note_to_midi('F'),       # Repeat or move
    note_to_midi('Bb'),      # Bb7 = Bb, D, F, Ab
    note_to_midi('D'),
    note_to_midi('F'),
    note_to_midi('Ab'),
]
piano_times = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
for t, pitch in zip(piano_times, piano_notes):
    note = Note(velocity=85, start=t, end=t + 0.25)
    piano.notes.append(note)

pm.instruments.append(piano)

# Sax: Melody - short motif, singable, no scale runs
# Motif: F -> B -> Eb -> F (in a rhythmic pattern)
# Time: 0.0 to 1.5 seconds (Bar 2)

sax_notes = [
    note_to_midi('F'),       # 0.0
    note_to_midi('Bb'),      # 0.5
    note_to_midi('Eb'),      # 1.0
    note_to_midi('F'),       # 1.5
]
sax_times = [0.0, 0.5, 1.0, 1.5]
for t, pitch in zip(sax_times, sax_notes):
    note = Note(velocity=100, start=t, end=t + 0.5)
    sax.notes.append(note)

# Add a rest before the resolution
rest_note = Note(velocity=0, start=1.5, end=2.0)
sax.notes.append(rest_note)

# Add the resolution in bar 3
sax_notes = [
    note_to_midi('Db'),      # 2.0
    note_to_midi('Bb'),      # 2.5
    note_to_midi('F'),       # 3.0
]
sax_times = [2.0, 2.5, 3.0]
for t, pitch in zip(sax_times, sax_notes):
    note = Note(velocity=100, start=t, end=t + 0.5)
    sax.notes.append(note)

pm.instruments.append(sax)

# Write the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file written as 'dante_russo_intro.mid'")
