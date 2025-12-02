
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: D minor (D Dorian? Or D minor? Let's go D minor for emotional tension)
key = 'D minor'

# Define time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Create instruments
bass = Instrument(program=Program.BASS_GUITAR_FRETLESS, is_drum=False)
piano = Instrument(program=Program.ELECTRIC_PIANO_2, is_drum=False)
drums = Instrument(program=Program.DRUMS, is_drum=True)
sax = Instrument(program=Program.TENOR_SAX, is_drum=False)

# Add instruments to the PrettyMIDI object
pm.instruments = [bass, piano, drums, sax]

# Define tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0.0)]

# Define the time per bar (1.5 seconds)
time_per_bar = 1.5
note_duration = 0.25  # quarter note
eighth_note = note_duration / 2
sixteenth_note = note_duration / 4

# --- Bar 1: Little Ray on drums only ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: Time 0.0 to 1.5 seconds
drum_notes = [
    # Kick on beat 1 (0.0)
    Note(36, 0.0, note_duration),
    # Snare on beat 2 (0.75)
    Note(38, 0.75, note_duration),
    # Kick on beat 3 (1.5)
    Note(36, 1.5, note_duration),
    # Snare on beat 4 (2.25)
    Note(38, 2.25, note_duration),
    # Hi-hat on every eighth: 0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625
    Note(42, 0.0, eighth_note),
    Note(42, 0.375, eighth_note),
    Note(42, 0.75, eighth_note),
    Note(42, 1.125, eighth_note),
    Note(42, 1.5, eighth_note),
    Note(42, 1.875, eighth_note),
    Note(42, 2.25, eighth_note),
    Note(42, 2.625, eighth_note),
]

# Add notes to drums instrument
for note in drum_notes:
    drums.notes.append(note)

# --- Bar 2: Everyone in. Sax takes the melody -- a short, searching motif in D minor. Let it hang. ---

# D minor scale: D (D4), Eb (Eb4), F (F4), G (G4), Ab (Ab4), Bb (Bb4), C (C5)
# Let’s define a short motif: D, Eb, F, G (ascending), then end on G (hanging)
# Time starts at 1.5 seconds (end of Bar 1)

# D4 (D4 = 62 MIDI note)
# Eb4 = 63
# F4 = 65
# G4 = 67

sax_notes = [
    Note(62, 1.5, note_duration),   # D4
    Note(63, 1.75, note_duration),  # Eb4
    Note(65, 2.0, note_duration),   # F4
    Note(67, 2.25, note_duration),  # G4
]

# Add to sax instrument
for note in sax_notes:
    sax.notes.append(note)

# --- Bar 2: Marcus on bass (walking line in D minor) ---
# Chromatic approach to D, then walking line with chromatic passing tones
# Time starts at 1.5

# Bass line: D (62) -> Eb (63) -> F (65) -> G (67) -> Ab (69) -> Bb (71) -> C (72) -> D (62)
bass_notes = [
    Note(62, 1.5, note_duration),
    Note(63, 1.75, note_duration),
    Note(65, 2.0, note_duration),
    Note(67, 2.25, note_duration),
    Note(69, 2.5, note_duration),
    Note(71, 2.75, note_duration),
    Note(72, 3.0, note_duration),
    Note(62, 3.25, note_duration),
]

# Add to bass
for note in bass_notes:
    bass.notes.append(note)

# --- Bar 2: Diane on piano (comping on 2 and 4, 7th chords, dissonant but resolving) ---

# D minor 7th chord: D (62), F (65), Bb (71), C (72)
# Let’s play that on beat 2 (start at 1.75) and 4 (start at 2.25)
# Add a dissonant passing chord (e.g., Bb7) with F# (68) to add tension

piano_notes = [
    # Dm7 on beat 2 (start at 1.75)
    Note(62, 1.75, note_duration),  # D
    Note(65, 1.75, note_duration),  # F
    Note(71, 1.75, note_duration),  # Bb
    Note(72, 1.75, note_duration),  # C

    # Dissonant passing chord (Bb7) on beat 3 (start at 2.0)
    Note(71, 2.0, note_duration),  # Bb
    Note(74, 2.0, note_duration),  # D
    Note(76, 2.0, note_duration),  # F#
    Note(78, 2.0, note_duration),  # A

    # Dm7 again on beat 4 (start at 2.25)
    Note(62, 2.25, note_duration),  # D
    Note(65, 2.25, note_duration),  # F
    Note(71, 2.25, note_duration),  # Bb
    Note(72, 2.25, note_duration),  # C
]

# Add to piano
for note in piano_notes:
    piano.notes.append(note)

# --- Bar 3-4: No additional notes in this example, but the sax can return to complete the motif if desired.

# Save the MIDI file
pm.write("dante_russo_4_bar_intro.mid")
