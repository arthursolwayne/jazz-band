
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: Dm (D minor)
# We'll use D minor scale and its related chords
# Dm7 = D, F, A, C
# Gm7 = G, Bb, D, F
# Cm7 = C, Eb, G, Bb
# F7 = F, A, C, E

# Define the four bars (each bar is 1.5 seconds at 160 BPM)
bar_duration = 1.5
total_duration = 4 * bar_duration

# Create instruments
# Drums (Little Ray)
drums = Instrument(program=Program.DRUMS, is_drum=True)
pm.instruments.append(drums)

# Bass (Marcus)
bass = Instrument(program=Program.BASS_GUITAR, name="Marcus")
pm.instruments.append(bass)

# Piano (Diane)
piano = Instrument(program=Program.PIANO, name="Diane")
pm.instruments.append(piano)

# Tenor Sax (Dante)
sax = Instrument(program=Program.SAXOPHONE, name="Dante")
pm.instruments.append(sax)

# ================ BAR 1: DRUMS ONLY =================
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Time: 0.0 to 1.5 seconds

# Kick on 1 and 3
kick_time1 = 0.0
kick_time2 = 0.75
drums.notes.append(Note(36, 100, kick_time1, kick_time1 + 0.25))
drums.notes.append(Note(36, 100, kick_time2, kick_time2 + 0.25))

# Snare on 2 and 4
snare_time1 = 0.375
snare_time2 = 1.125
drums.notes.append(Note(38, 100, snare_time1, snare_time1 + 0.25))
drums.notes.append(Note(38, 100, snare_time2, snare_time2 + 0.25))

# Hi-hat on every 8th
hihat_time = [0.0, 0.375, 0.75, 1.125]
for t in hihat_time:
    drums.notes.append(Note(42, 70, t, t + 0.1))

# ================ BAR 2: EVERYONE IN =================
# Time: 1.5 to 3.0 seconds

# Bass (Marcus) - Walking line in Dm: D2, F2, G2, A2, C2, D2, F2, G2
# Each note is 0.375 seconds
bass_notes = [38, 41, 43, 45, 47, 38, 41, 43]
for i, note_num in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(Note(note_num, 80, start, end))

# Piano (Diane) - Open voicings in Dm, Gm, Cm, F7
# Bar 2: Dm7 (D, F, A, C) - D2, F2, A2, C3
# Bar 3: Gm7 (G, Bb, D, F) - G2, Bb2, D2, F2
# Bar 4: Cm7 (C, Eb, G, Bb) - C2, Eb2, G2, Bb2
# Bar 4: F7 (F, A, C, E) - F2, A2, C2, E2

# Bar 2: Dm7
piano.notes.append(Note(45, 100, 1.5, 1.5 + 0.25))
piano.notes.append(Note(48, 100, 1.5, 1.5 + 0.25))
piano.notes.append(Note(50, 100, 1.5, 1.5 + 0.25))
piano.notes.append(Note(52, 100, 1.5, 1.5 + 0.25))

# Bar 3: Gm7
piano.notes.append(Note(49, 100, 2.25, 2.25 + 0.25))
piano.notes.append(Note(51, 100, 2.25, 2.25 + 0.25))
piano.notes.append(Note(45, 100, 2.25, 2.25 + 0.25))
piano.notes.append(Note(48, 100, 2.25, 2.25 + 0.25))

# Bar 4: Cm7
piano.notes.append(Note(47, 100, 3.0, 3.0 + 0.25))
piano.notes.append(Note(50, 100, 3.0, 3.0 + 0.25))
piano.notes.append(Note(49, 100, 3.0, 3.0 + 0.25))
piano.notes.append(Note(51, 100, 3.0, 3.0 + 0.25))

# ================ BAR 2: SAX (Dante) - YOUR MOMENT =================
# Dm scale: D, E, F, G, A, Bb, C
# Motif: D, F, E, G — short, emotional, leaves it hanging

sax_notes = [
    Note(50, 100, 1.5, 1.65),     # D (rest of bar before entering)
    Note(52, 100, 1.75, 1.9),     # F
    Note(51, 100, 1.9, 2.05),     # E
    Note(53, 100, 2.05, 2.2),     # G
    Note(50, 100, 2.2, 2.35),     # D again
    Note(55, 100, 2.35, 2.5),     # Bb — tension
    Note(50, 100, 2.5, 2.65),     # D again
    Note(52, 100, 2.65, 2.8),     # F again
    Note(51, 100, 2.8, 2.95),     # E — leaves it hanging
    Note(53, 100, 2.95, 3.05),    # G — resolves
]

for note in sax_notes:
    sax.notes.append(note)

# ================ BAR 3 & 4: DRUMS CONTINUE =================
# Keep the same pattern, slightly more energy

# Bar 3: Kick on 1 and 3 (2.25 and 3.0)
drums.notes.append(Note(36, 100, 2.25, 2.25 + 0.25))
drums.notes.append(Note(36, 100, 3.0, 3.0 + 0.25))

# Snare on 2 and 4 (2.625 and 3.375)
drums.notes.append(Note(38, 100, 2.625, 2.625 + 0.25))
drums.notes.append(Note(38, 100, 3.375, 3.375 + 0.25))

# Hi-hat on every 8th
hihat_time = [2.25, 2.625, 3.0, 3.375]
for t in hihat_time:
    drums.notes.append(Note(42, 70, t, t + 0.1))

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file saved as 'dante_intro.mid'")
print("This 4-bar intro is built with emotional contrast, rests, and a unique sax motif.")
print("It's meant to make Wayne lean forward — it's the kind of intro that starts a conversation.")
print("Play it loud, play it proud, and make the Cellar remember tonight.")
