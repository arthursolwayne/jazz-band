
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Define tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=time_signature[0], denominator=time_signature[1], time=0)]

# Set tempo
pm.tempo_changes = [pretty_midi.TempoChange(tempo=tempo, time=0)]

# Define key: D Major
key = 'D'

# Instrument assignment
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS, is_drum=False)
piano = Instrument(program=Program.ACOUSTIC_PIANO, is_drum=False)
sax = Instrument(program=Program.TENOR_SAX, is_drum=False)

pm.instruments = [drums, bass, piano, sax]

# Define note durations and timing
note_duration = 0.375  # 1/8 note at 160 BPM
bar_length = 1.5  # 4/4 bar at 160 BPM
bar_start = 0.0
bar_end = bar_length

# --- BAR 1: DRUMS ONLY (build tension) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    # Bar 1
    Note(36, 0.0, note_duration),  # Kick on 1
    Note(38, 0.375, note_duration),  # Snare on 2
    Note(42, 0.0, note_duration),  # Hihat on 1
    Note(42, 0.375, note_duration),  # Hihat on 2
    Note(42, 0.75, note_duration),  # Hihat on 3
    Note(36, 0.75, note_duration),  # Kick on 3
    Note(38, 1.125, note_duration),  # Snare on 4
    Note(42, 1.125, note_duration),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# --- BAR 2: INTRO - SAX TAKES LEAD ---
# D Major scale: D, E, F#, G, A, B, C#, D
# You play a short phrase: D - F# - G - rest
# Rhythmic pattern: D (8th), F# (8th), G (8th), rest (8th)
sax_notes = [
    Note(62, 0.0, note_duration),  # D4
    Note(66, 0.375, note_duration),  # F#4
    Note(67, 0.75, note_duration),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# --- BAR 3: INTRO CONTINUED - BASS AND PIANO JOIN IN ---
# Bass: Walking line in D major, chromatic approach
# D -> C# -> B -> A -> G -> F# -> E -> D
# Play each note on 8th notes
bass_notes = [
    Note(62, 1.5, note_duration),  # D4
    Note(61, 1.875, note_duration),  # C#4
    Note(60, 2.25, note_duration),  # B4
    Note(59, 2.625, note_duration),  # A4
    Note(57, 3.0, note_duration),  # G4
    Note(56, 3.375, note_duration),  # F#4
    Note(55, 3.75, note_duration),  # E4
    Note(53, 4.125, note_duration),  # D4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar starts at 1.5, so 2 and 4 are at 0.375 and 1.125 in the bar
# D7 (D, F#, A, C#) on beat 2
# D7 again on beat 4
piano_notes = [
    Note(62, 1.875, note_duration),  # D4
    Note(66, 1.875, note_duration),  # F#4
    Note(67, 1.875, note_duration),  # A4
    Note(61, 1.875, note_duration),  # C#4
    Note(62, 2.625, note_duration),  # D4
    Note(66, 2.625, note_duration),  # F#4
    Note(67, 2.625, note_duration),  # A4
    Note(61, 2.625, note_duration),  # C#4
]
for note in piano_notes:
    piano.notes.append(note)

# --- BAR 4: RESOLUTION - SAX FINISHES THE MOTIF ---
# D - F# - G - A (a short melody with a hint of resolution)
# D on beat 1, F# on 2, G on 3, A on 4
sax_notes = [
    Note(62, 3.0, note_duration),  # D4
    Note(66, 3.375, note_duration),  # F#4
    Note(67, 3.75, note_duration),  # G4
    Note(69, 4.125, note_duration),  # A4
]
for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
