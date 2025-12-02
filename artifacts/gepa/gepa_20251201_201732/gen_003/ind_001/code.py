
import pretty_midi

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define the key: D minor (but we'll use D mixolydian with a bit of tension for a moody, mysterious feel)
# D mixolydian: D, E, F#, G, A, B, C
# We'll use D minor (D, E, F, G, A, Bb, C) for a darker, more introspective sound

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')

# Add instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define BPM and time parameters
bpm = 160
beat = 60.0 / bpm  # seconds per beat
bar_length = beat * 4  # seconds per bar
note_length = beat / 2  # quarter note
rest = beat * 0.5  # half rest
eighth = beat / 2

# --- BAR 1: Little Ray alone (drums) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0, end=note_length),
              pretty_midi.Note(velocity=100, pitch=36, start=beat * 2, end=beat * 2 + note_length)]
drums.notes.extend(kick_notes)

# Snare
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=beat, end=beat + note_length),
               pretty_midi.Note(velocity=100, pitch=38, start=beat * 3, end=beat * 3 + note_length)]
drums.notes.extend(snare_notes)

# Hihat
hihat_notes = [pretty_midi.Note(velocity=90, pitch=42, start=i * eighth, end=i * eighth + eighth) for i in range(8)]
drums.notes.extend(hihat_notes)

# --- BAR 2: Enter the band. You take the melody -- short motif, make it sing ---
# Tenor sax melody: Start with "D" (62), then "F" (65), then "G" (67), then rest on "A" (69)
# This is a simple, mysterious motif with space and tension

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=0, end=note_length),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=note_length, end=note_length * 2),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=note_length * 2, end=note_length * 3),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=note_length * 3, end=note_length * 3 + rest),  # A (rest after)
]
sax.notes.extend(sax_notes)

# --- BAR 2: Diane (piano) on comping (bar 2, comp on 2 and 4) ---
# Open voicings, different chord each bar (resolve on the last)

# Bar 2: D minor 7 (D, F, A, C) => D, F, A, C in root position
# Open voicing: D (62), F (65), A (69), C (60) => drop 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=note_length, end=note_length + eighth),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=note_length, end=note_length + eighth),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=note_length, end=note_length + eighth),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=note_length, end=note_length + eighth),  # C
]
piano.notes.extend(piano_notes)

# --- BAR 3: Marcus (bass) on walking line (D2-G2, MIDI 38-43) roots and fifths with chromatic approaches ---
# Bar 3: D minor -> G minor (G, Bb, D) -> chromatic approach to G

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=beat * 2, end=beat * 2 + note_length),  # D (root)
    pretty_midi.Note(velocity=80, pitch=64, start=beat * 2 + note_length, end=beat * 2 + note_length * 2),  # E (chromatic)
    pretty_midi.Note(velocity=80, pitch=67, start=beat * 2 + note_length * 2, end=beat * 2 + note_length * 3),  # G (fifth of D)
    pretty_midi.Note(velocity=80, pitch=65, start=beat * 2 + note_length * 3, end=beat * 2 + note_length * 4),  # F (chromatic)
]
bass.notes.extend(bass_notes)

# --- BAR 3: Diane (piano) comp on 2 and 4 (bar 3) ---
# III7 (F7) -> F, A, C, E

piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=beat * 2 + note_length, end=beat * 2 + note_length + eighth),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=beat * 2 + note_length, end=beat * 2 + note_length + eighth),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=beat * 2 + note_length, end=beat * 2 + note_length + eighth),  # E
    pretty_midi.Note(velocity=90, pitch=66, start=beat * 2 + note_length, end=beat * 2 + note_length + eighth),  # C
]
piano.notes.extend(piano_notes)

# --- BAR 4: Diane (piano) comp on 2 and 4 (bar 4) ---
# V7 (A7) -> A, C#, E, G

piano_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=beat * 3 + note_length, end=beat * 3 + note_length + eighth),  # C#
    pretty_midi.Note(velocity=90, pitch=72, start=beat * 3 + note_length, end=beat * 3 + note_length + eighth),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=beat * 3 + note_length, end=beat * 3 + note_length + eighth),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=beat * 3 + note_length, end=beat * 3 + note_length + eighth),  # G
]
piano.notes.extend(piano_notes)

# --- BAR 4: Marcus (bass) on walking line (roots and fifths) ---
# Bar 4: A7 -> D minor 7 again (chromatic approach to D)

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=beat * 3, end=beat * 3 + note_length),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=beat * 3 + note_length, end=beat * 3 + note_length * 2),  # G (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=beat * 3 + note_length * 2, end=beat * 3 + note_length * 3),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=beat * 3 + note_length * 3, end=beat * 3 + note_length * 4),  # E (chromatic)
]
bass.notes.extend(bass_notes)

# --- BAR 4: You (sax) — finish the motif with a return to D, suspended light, open-ended ---
# End the motif with a D, then leave it hanging on a rest. Make it sing.

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=beat * 3, end=beat * 3 + note_length),
    pretty_midi.Note(velocity=100, pitch=62, start=beat * 3 + note_length, end=beat * 3 + note_length * 2),
    pretty_midi.Note(velocity=100, pitch=62, start=beat * 3 + note_length * 2, end=beat * 3 + note_length * 3),
]
sax.notes.extend(sax_notes)

# Save the MIDI
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid' — lean forward, Wayne.")
