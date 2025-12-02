
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F Major
key_signature = pretty_midi.KeySignature(key_number=1)  # F Major (key_number=1)
pm.key_signature_changes.append(key_signature)

# Define the time signature (4/4)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature_changes.append(time_signature)

# Define the tempo (160 BPM)
pm.tempo_changes.append(pretty_midi.TempoChange(tempo=160, time=0))

# Define the time per beat and per bar
beats_per_bar = 4
notes_per_beat = 4  # quarter notes
beat_duration = 60.0 / 160  # 0.375 seconds per beat
bar_duration = beat_duration * beats_per_bar  # 1.5 seconds per bar

# Define instrument programs
tenor_sax_program = 64  # Tenor saxophone
bass_program = 33  # Acoustic bass
piano_program = 0  # Acoustic piano
drums_program = 0  # Drums

# Create instrument tracks
tenor_track = pretty_midi.Instrument(program=tenor_sax_program)
bass_track = pretty_midi.Instrument(program=bass_program)
piano_track = pretty_midi.Instrument(program=piano_program)
drum_track = pretty_midi.Instrument(program=drums_program, is_drum=True)

# Add instruments to the PrettyMIDI object
pm.instruments.append(tenor_track)
pm.instruments.append(bass_track)
pm.instruments.append(piano_track)
pm.instruments.append(drum_track)

#======================== DRUMS: Bar 1 (0 - 1.5s) ========================
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on beats 1 and 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0, end=0.25),
              pretty_midi.Note(velocity=100, pitch=36, start=1.0, end=1.25)]

# Snare on beats 2 and 4
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=0.5, end=0.75),
               pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75)]

# Hi-hat on every eighth note
hihat_notes = [pretty_midi.Note(velocity=90, pitch=42, start=i*0.375, end=i*0.375 + 0.125) for i in range(6)]

# Add all to drum track
drum_track.notes.extend(kick_notes)
drum_track.notes.extend(snare_notes)
drum_track.notes.extend(hihat_notes)

#======================== BASS: Bar 1 (0 - 1.5s) ========================
# Walking line, chromatic approaches, unique rhythmic placements, no repetition

# Bar 1: F -> G -> Ab -> A -> Bb -> B -> C -> D (chromatic walking up)
# Placed on upbeats and offbeats to keep it moving, not predictable

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=0.0, end=0.125),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=0.25, end=0.375),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=0.5, end=0.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=0.75, end=0.875),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=1.0, end=1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.25, end=1.375),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=1.75, end=1.875)   # D
]

bass_track.notes.extend(bass_notes)

#======================== PIANO: Bars 2-4 (1.5 - 4.5s) ========================
# 7th chords, comp on 2 and 4, space, not density

# Define chord voicings: F7, Bb7, Eb7, Ab7 (no modulation, just F mixolydian)
# Chord on 2 and 4 (beat 2 and beat 4)

# F7 (F A C Eb) - Bb7 (Bb D F Ab) - Eb7 (Eb G Bb Db) - Ab7 (Ab C Eb G)

# Bar 2 (1.5 - 3.0s)
# Chord on beat 2 (1.5s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75)   # Eb
]

# Bar 3 (3.0 - 4.5s)
# Chord on beat 2 (3.0s)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25)   # Ab
])

# Bar 4 (4.5 - 6.0s)
# Chord on beat 2 (4.5s)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75)   # Db
])

piano_track.notes.extend(piano_notes)

#======================== SAX: Bars 2-4 (1.5 - 4.5s) ========================
# Your motif: F - Ab - Bb - C (motif), played on beat 1, left hanging on beat 2, then resolved on beat 4

# Bar 2 - Motif starts (beat 1)
tenor_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0)   # C
]

# Bar 3 - No notes (space)
# Bar 4 - Return and resolve on beat 4
tenor_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625))  # F

tenor_track.notes.extend(tenor_notes)

# Save the MIDI file
pm.write("jazz_intro_f_major.mid")
