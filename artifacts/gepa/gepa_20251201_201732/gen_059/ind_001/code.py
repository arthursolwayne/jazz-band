
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor (Fm)
key = 'Fm'

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

# Add the time signature
pm.time_signature_changes.append(time_signature)

# Define the tempo (160 BPM)
pm.tempo_changes.append(pretty_midi.TempoChange(tempo=160, time=0))

# Create instruments
bass = Instrument(program=Program.BASS, is_drum=False)
piano = Instrument(program=Program.ACOUSTIC_GRAND_PIANO, is_drum=False)
drums = Instrument(program=Program.DRUMS, is_drum=True)
sax = Instrument(program=Program.TENOR_SAX, is_drum=False)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Define the timing for 160 BPM (each beat is 0.375 seconds)
beat = 0.375
bar = beat * 4  # 1.5 seconds per bar
total_time = bar * 4  # 6 seconds

# -----------------------------
# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# -----------------------------
# Drums: Bar 1 (0 to 1.5s)
drum_notes = [
    # Kick on 1 and 3
    Note(36, 0, beat * 0.5),
    Note(36, 0, beat * 2.5),
    # Snare on 2 and 4
    Note(38, 0, beat * 1.0),
    Note(38, 0, beat * 3.0),
    # Hi-Hat on every eighth note
    Note(42, 0, beat * 0.0),
    Note(42, 0, beat * 0.5),
    Note(42, 0, beat * 1.0),
    Note(42, 0, beat * 1.5),
    Note(42, 0, beat * 2.0),
    Note(42, 0, beat * 2.5),
    Note(42, 0, beat * 3.0),
    Note(42, 0, beat * 3.5),
]

for note in drum_notes:
    drums.notes.append(note)

# -----------------------------
# Bar 2: Everyone enters
# -----------------------------
# Bass (Marcus): Walking line in Fm (F, Ab, D, C, G, Eb, Bb, E)
# Root and fifths with chromatic approaches
# Bar 2 (1.5s to 3s)
bass_notes = [
    Note(46, 1.5, beat * 0.0),  # F2
    Note(44, 1.5, beat * 0.5),  # Eb2
    Note(50, 1.5, beat * 1.0),  # D2
    Note(48, 1.5, beat * 1.5),  # C2
    Note(52, 1.5, beat * 2.0),  # G2
    Note(51, 1.5, beat * 2.5),  # F#2 (chromatic approach to G)
    Note(56, 1.5, beat * 3.0),  # Bb2
    Note(55, 1.5, beat * 3.5),  # A#2 (chromatic approach to Bb)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chords each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    Note(64, 1.5, beat * 0.0),  # F4
    Note(76, 1.5, beat * 0.0),  # Ab4
    Note(72, 1.5, beat * 0.0),  # C4
    Note(74, 1.5, beat * 0.0),  # D4
    Note(60, 1.5, beat * 0.0),  # C3 (left hand)
    Note(57, 1.5, beat * 0.0),  # Bb3
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): The motif — concise, memorable, with tension
# Motif: F - Ab - Bb - C (Fm scale, but spaced with tension)
sax_notes = [
    Note(64, 1.5, beat * 0.0),  # F4
    Note(69, 1.5, beat * 0.5),  # Bb4 (chromatic tension)
    Note(66, 1.5, beat * 1.0),  # Ab4
    Note(67, 1.5, beat * 1.5),  # Bb4 again (space for breath)
    Note(64, 1.5, beat * 2.0),  # F4 (reprise)
]

# Add a slight delay before the resolution
sax_notes.append(Note(69, 1.5, beat * 3.0))  # Bb4 (resolution)

for note in sax_notes:
    sax.notes.append(note)

# -----------------------------
# Bar 3: Piano continues with a new chord
# Fm7 -> Bb7 (tritone substitution)
# -----------------------------
# Bar 3 (3.0s to 4.5s)
piano_notes = [
    Note(67, 3.0, beat * 0.0),  # Bb4
    Note(71, 3.0, beat * 0.0),  # D4
    Note(76, 3.0, beat * 0.0),  # Ab4
    Note(79, 3.0, beat * 0.0),  # G4
    Note(60, 3.0, beat * 0.0),  # C3
    Note(57, 3.0, beat * 0.0),  # Bb3
]

for note in piano_notes:
    piano.notes.append(note)

# -----------------------------
# Bar 4: Sax resolves the motif, everyone holds
# -----------------------------
# Sax: F - Ab - Bb - C (resolve the tension)
sax_notes = [
    Note(64, 4.5, beat * 0.0),  # F4
    Note(66, 4.5, beat * 0.5),  # Ab4
    Note(67, 4.5, beat * 1.0),  # Bb4
    Note(67, 4.5, beat * 1.5),  # Bb4 (hold)
    Note(64, 4.5, beat * 2.0),  # F4 (resolution)
]

for note in sax_notes:
    sax.notes.append(note)

# -----------------------------
# Write the MIDI file
# -----------------------------
pm.write("jazz_intro_in_Fm.mid")

print("✅ MIDI file 'jazz_intro_in_Fm.mid' created successfully.")
