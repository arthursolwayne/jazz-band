
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds per bar (160 BPM, 4/4 time)
time_per_bar = 6.0  # 6 seconds per bar
time_per_beat = time_per_bar / 4  # 1.5 seconds per beat
time_per_eighth = time_per_beat / 2  # 0.75 seconds per eighth note

# Define the key: D major
key = 'D'

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
piano = Instrument(program=Program.PIANO)
bass = Instrument(program=Program.BASS)
sax = Instrument(program=Program.SAXOPHONE_ALTO)
pm.instruments = [drums, piano, bass, sax]

# --- BAR 1: DRUMS ONLY — Mysterious, urgent, incomplete ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [Note(36, 0.25, 0.0), Note(36, 0.25, 2.0)]  # Beats 1 and 3
snare_notes = [Note(38, 0.25, 1.0), Note(38, 0.25, 3.0)]  # Beats 2 and 4
hihat_notes = [Note(42, 0.125, i * time_per_eighth) for i in range(8)]

drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# --- BAR 2: FULL ENSEMBLE — Piano, Bass, Drums continue ---
# Bass: Walking line in D major
bass_notes = [
    Note(38, 0.75, 6.0),  # D2 (root)
    Note(40, 0.75, 7.5),  # F#2 (third)
    Note(39, 0.75, 9.0),  # E2 (chromatic approach)
    Note(41, 0.75, 10.5), # G2 (fifth)
    Note(38, 0.75, 12.0), # D2 (root again)
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last chord
# Bar 2: D7 (D F# A C#)
piano_notes = [
    Note(62, 0.75, 6.0),  # D4
    Note(66, 0.75, 6.0),  # F#4
    Note(69, 0.75, 6.0),  # A4
    Note(71, 0.75, 6.0),  # C#5
]

# Bar 2: D7 resolve to G7 on beat 4
piano_notes.extend([
    Note(67, 0.75, 10.5), # G4
    Note(71, 0.75, 10.5), # B4
    Note(74, 0.75, 10.5), # D5
    Note(76, 0.75, 10.5), # F#5
])

piano.notes.extend(piano_notes)

# Drums continue in Bar 2
drums_notes = [
    Note(36, 0.25, 6.0), Note(36, 0.25, 8.0),  # Kick on 1 and 3
    Note(38, 0.25, 7.0), Note(38, 0.25, 9.0),  # Snare on 2 and 4
    Note(42, 0.125, i * time_per_eighth + 6.0) for i in range(8)  # Hihat
]
drums.notes.extend(drums_notes)

# --- BAR 3: SAXOPHONE ENTERS — Concise, emotional, unresolved ---
# Motif: D - F# - A (melodic minor feel), then G (leading tone)
sax_notes = [
    Note(62, 0.5, 12.0),  # D4
    Note(66, 0.5, 13.5),  # F#4
    Note(69, 0.5, 15.0),  # A4
    Note(67, 0.5, 16.5),  # G4
]

sax.notes.extend(sax_notes)

# --- BAR 4: SAX CONTINUES — Resolves slightly, leaves space ---
# Continue the motif with a small resolution
sax_notes.extend([
    Note(62, 0.5, 18.0),  # D4 (return to root)
    Note(66, 0.5, 19.5),  # F#4
    Note(69, 0.5, 21.0),  # A4
    Note(71, 0.5, 22.5),  # C#5 (up a half step, unresolved)
])

sax.notes.extend(sax_notes)

# Save the MIDI file
pm.write("intro_born_in_the_dark.mid")

print("MIDI file written to 'intro_born_in_the_dark.mid'")
