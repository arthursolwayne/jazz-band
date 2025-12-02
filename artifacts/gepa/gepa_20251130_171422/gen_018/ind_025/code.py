
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key signature: F major (no sharps or flats)
midi.key_signature_changes = [pretty_midi.KeySignature(0, 0, 0)]  # F major

# Define instrument tracks
saxophone_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')

sax_track = pretty_midi.Instrument(program=saxophone_program)
bass_track = pretty_midi.Instrument(program=bass_program)
piano_track = pretty_midi.Instrument(program=piano_program)
drum_track = pretty_midi.Instrument(program=drums_program)

# Add tracks
midi.instruments = [sax_track, bass_track, piano_track, drum_track]

# Time in seconds per bar (160 BPM = 60 / 160 = 0.375 seconds per beat, 4/4 time)
bar_length = 0.375 * 4  # 1.5 seconds per bar
total_length = bar_length * 4  # 6 seconds

# --- DRUMS: Little Ray ---
# Bar 1: Just a snare on beat 2, hihat on 8th notes, kick on 1 and 3
drum_notes = []
bar_start = 0.0

# Bar 1: Kick on 1 and 3, snare on 2, hihat on all 8ths
drum_notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.375))  # Kick on 1
drum_notes.append(pretty_midi.Note(velocity=80, pitch=68, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))  # Snare on 2
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start, end=bar_start + 0.375))  # Hihat on 1
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))  # Hihat on 2
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))  # Hihat on 3
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))  # Hihat on 4
drum_notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))  # Kick on 3

# Bar 2: Full energy, kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 1.5, end=bar_start + 1.5 + 0.375))  # Kick on 1
drum_notes.append(pretty_midi.Note(velocity=80, pitch=68, start=bar_start + 1.875, end=bar_start + 1.875 + 0.375))  # Snare on 2
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 1.5, end=bar_start + 1.5 + 0.375))  # Hihat on 1
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 1.875, end=bar_start + 1.875 + 0.375))  # Hihat on 2
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 2.25, end=bar_start + 2.25 + 0.375))  # Hihat on 3
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 2.625, end=bar_start + 2.625 + 0.375))  # Hihat on 4
drum_notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 2.625, end=bar_start + 2.625 + 0.375))  # Kick on 3

# Bar 3: Same pattern
bar_start = 3.0
drum_notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.375))  # Kick on 1
drum_notes.append(pretty_midi.Note(velocity=80, pitch=68, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))  # Snare on 2
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start, end=bar_start + 0.375))  # Hihat on 1
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))  # Hihat on 2
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))  # Hihat on 3
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))  # Hihat on 4
drum_notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))  # Kick on 3

# Bar 4: Same pattern
bar_start = 4.5
drum_notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.375))  # Kick on 1
drum_notes.append(pretty_midi.Note(velocity=80, pitch=68, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))  # Snare on 2
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start, end=bar_start + 0.375))  # Hihat on 1
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))  # Hihat on 2
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))  # Hihat on 3
drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))  # Hihat on 4
drum_notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))  # Kick on 3

# Add the notes to the drum track
drum_track.notes = drum_notes

# --- BASS: Marcus ---
# Chromatic walking line, no repeated notes or intervals
# In F major, use Dorian mode for a dark, bluesy feel

# Bar 1: F -> E → D → C (chromatic descending)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=0.0, end=0.375),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=0.375, end=0.75),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=0.75, end=1.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.125, end=1.5),  # C
]

# Bar 2: C → B → A → G (chromatic descending)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875)),  # C
bass_notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25)),  # B
bass_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625)),  # A
bass_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0)),  # G

# Bar 3: G → F# → F → E
bass_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375)),  # G
bass_notes.append(pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75)),  # F#
bass_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125)),  # F (again, chromatic approach)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5)),  # E

# Bar 4: E → D → C → B
bass_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875)),  # E
bass_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25)),  # D
bass_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625)),  # C
bass_notes.append(pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0)),  # B

# Add notes to bass track
bass_track.notes = bass_notes

# --- PIANO: Diane ---
# Comping with 7th chords on 2 and 4, dark and rich
# F minor 7, Bb minor 7, Eb minor 7, Ab minor 7 — all in F Dorian
# Rest on 1 and 3

piano_notes = []

# Bar 1: Fm7 (F, Ab, C, Eb)
# Play on beat 2 and 4
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=0.75, end=1.125))  # F
piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=0.75, end=1.125))  # Ab
piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=0.75, end=1.125))  # C
piano_notes.append(pretty_midi.Note(velocity=80, pitch=60, start=0.75, end=1.125))  # Eb
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875))  # F
piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875))  # Ab
piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875))  # C
piano_notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875))  # Eb

# Bar 2: Bbm7 (Bb, Db, F, Ab)
piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625))  # Bb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625))  # Db
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625))  # F
piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625))  # Ab
piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0))  # Bb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0))  # Db
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0))  # F
piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0))  # Ab

# Bar 3: Ebm7 (Eb, Gb, Bb, Db)
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125))  # Eb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125))  # Gb
piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125))  # Bb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125))  # Db
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5))  # Eb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.5))  # Gb
piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5))  # Bb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5))  # Db

# Bar 4: Abm7 (Ab, B, Db, F)
piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625))  # Ab
piano_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625))  # B
piano_notes.append(pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625))  # Db
piano_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0))  # Ab
piano_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0))  # B
piano_notes.append(pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0))  # Db
piano_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0))  # F

# Add notes to piano track
piano_track.notes = piano_notes

# --- SAX: Dante ---
# Motif: F, G#, Bb, C — searching, with a rest in the middle
# Play on beat 1, skip beat 2, play beat 3 with a slight delay, end on beat 4

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=0.0, end=0.375),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=0.75, end=1.125),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=6.0),  # G#
]

# Add notes to sax track
sax_track.notes = sax_notes

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' has been generated.")
