
import pretty_midi

# Initialize the MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum mappings
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray (Drums only)
# Start at 0.0, duration 1.5 seconds
drum_notes = []
for time in [0.0, 0.75, 1.5]:  # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.15))
for time in [0.375, 1.125]:  # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.15))
for time in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5]:  # Hi-hat on every 8th note
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.05))
drums.notes.extend(drum_notes)

# Bar 2: Full Quartet (1.5 - 3.0s)

# SAX: Tenor sax melody (Fm key, 7th chord color)
# Motif: Fm7 -> Ab -> Bb -> C (Fm7 arpeggio, with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.75),  # F7 (F, Ab, Bb, C)
    pretty_midi.Note(velocity=95, pitch=81, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=82, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=87, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=84, start=2.5, end=2.75),  # F (return to F, leave it hanging)
    pretty_midi.Note(velocity=95, pitch=81, start=2.75, end=3.0),  # Ab (resolve or not?)
]
sax.notes.extend(sax_notes)

# BASS: Walking line, chromatic approach to Fm7
# Fm7: F, Ab, Bb, Db
# Walking line: E -> F -> Gb -> Ab -> Bb -> C -> Db -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=64, start=1.5, end=1.75),  # E (chromatic approach to F)
    pretty_midi.Note(velocity=75, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=75, pitch=66, start=2.0, end=2.25),  # Gb (chromatic)
    pretty_midi.Note(velocity=75, pitch=68, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=75, pitch=71, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=75, pitch=72, start=2.75, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# PIANO: Comping on 2 and 4 with Fm7 chords
# Fm7: F, Ab, Bb, Db
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Db
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Full Quartet (3.0 - 4.5s)
# SAX: Repeat the motif but with a slight variation (delayed resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=95, pitch=81, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=82, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=87, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=84, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=95, pitch=81, start=4.25, end=4.5),  # Ab
]
sax.notes.extend(sax_notes)

# BASS: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=72, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=75, pitch=73, start=3.25, end=3.5),  # Db
    pretty_midi.Note(velocity=75, pitch=74, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=75, pitch=76, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=75, pitch=77, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=75, pitch=79, start=4.25, end=4.5),  # Ab
]
bass.notes.extend(bass_notes)

# PIANO: Comping on 2 and 4 again
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # Db
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),  # Db
]
piano.notes.extend(piano_notes)

# Bar 4: Full Quartet (4.5 - 6.0s)
# SAX: Resolve the motif — bring it back with a little twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=95, pitch=81, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=82, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=87, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=84, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=95, pitch=81, start=5.75, end=6.0),  # Ab
]
sax.notes.extend(sax_notes)

# BASS: Walking line resolves on F
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=76, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=75, pitch=77, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=75, pitch=79, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=75, pitch=82, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=75, pitch=84, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=75, pitch=84, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# PIANO: Comping resolves with Fm7 on the last beat
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # Db
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.75, end=6.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),  # Db
]
piano.notes.extend(piano_notes)

# Add all instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
