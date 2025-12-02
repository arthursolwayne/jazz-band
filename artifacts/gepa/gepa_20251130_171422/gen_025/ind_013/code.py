
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Time signature and tempo
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define the key: F major (F, G, A, Bb, C, D, E)
# We'll use F major for the piece

# Create instruments
bass_program = Program(33)  # Upright Bass
piano_program = Program(0)  # Acoustic Piano
drums_program = Program(0)  # Acoustic Grand Piano (for hihat)
sax_program = Program(69)   # Tenor Saxophone

# Create instruments
bass_instrument = Instrument(program=bass_program)
piano_instrument = Instrument(program=piano_program)
drums_instrument = Instrument(program=drums_program)
sax_instrument = Instrument(program=sax_program)

pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# Define tempo and time per bar
BPM = 160
time_per_beat = 60.0 / BPM
time_per_bar = 4 * time_per_beat  # 4/4 time

# Define beat times for 4 bars
bar_times = [i * time_per_bar for i in range(4)]

# -------------------
# DRUMS: Little Ray
# -------------------

# Hihat on every eighth note
# Kick on 1 and 3, snare on 2 and 4

def add_drums(instrument, bar_times):
    for bar_idx, bar_time in enumerate(bar_times):
        # Kick on 1 and 3
        kick_time = bar_time
        kick_note = Note(36, 100, kick_time, kick_time + 0.1)
        instrument.notes.append(kick_note)

        kick_time = bar_time + time_per_beat * 2
        kick_note = Note(36, 100, kick_time, kick_time + 0.1)
        instrument.notes.append(kick_note)

        # Snare on 2 and 4
        snare_time = bar_time + time_per_beat
        snare_note = Note(38, 100, snare_time, snare_time + 0.1)
        instrument.notes.append(snare_note)

        snare_time = bar_time + time_per_beat * 3
        snare_note = Note(38, 100, snare_time, snare_time + 0.1)
        instrument.notes.append(snare_note)

        # Hihat on every eighth
        for i in range(8):
            hihat_time = bar_time + (i * time_per_beat / 2)
            hihat_note = Note(42, 80, hihat_time, hihat_time + 0.05)
            instrument.notes.append(hihat_note)

add_drums(drums_instrument, bar_times)

# -------------------
# BASS: Marcus
# -------------------

def add_bass(instrument, bar_times):
    # Walking line in F major (F, G, A, Bb, C, D, E)
    # F - G - A - Bb - C - D - E - F
    # Each note 1/4 note, with chromatic variations and space

    bass_notes = [
        # Bar 1
        (45, 0.0),      # F (muted, tension)
        (47, 0.25),     # G
        (49, 0.5),      # A
        (48, 0.75),     # Bb
        # Bar 2
        (50, 1.0),      # C
        (52, 1.25),     # D
        (53, 1.5),      # E
        (50, 1.75),     # C (chromatic approach)
        # Bar 3
        (48, 2.0),      # Bb
        (49, 2.25),     # A
        (50, 2.5),      # C
        (52, 2.75),     # D
        # Bar 4
        (53, 3.0),      # E
        (54, 3.25),     # F#
        (52, 3.5),      # D
        (50, 3.75),     # C (resting on the edge)
    ]

    for note, time in bass_notes:
        duration = 0.25
        bass_note = Note(note, 80, time, time + duration)
        instrument.notes.append(bass_note)

add_bass(bass_instrument, bar_times)

# -------------------
# PIANO: Diane
# -------------------

def add_piano(instrument, bar_times):
    # 7th chords on 2 and 4, with dissonance and resolution
    # F7 (F, A, C, E♭) on bar 2
    # A7 (A, C#, E, G) on bar 4

    # Bar 1: tension with dissonant voicings
    # Bar 2: F7 (C - F - A - E♭)
    # Bar 3: Chromatic passing chords
    # Bar 4: A7 (G - E - C# - A)

    # Bar 1 - Dissonant cluster
    bar_1_notes = [
        (60, 0.0, 50),   # C
        (63, 0.0, 60),   # E♭
        (65, 0.0, 55),   # G
        (67, 0.0, 65),   # A
        (69, 0.0, 75),   # B
    ]

    # Bar 2 - F7 (C - F - A - E♭)
    bar_2_notes = [
        (60, 1.0, 85),   # C
        (65, 1.0, 75),   # G
        (67, 1.0, 85),   # A
        (63, 1.0, 85),   # E♭
    ]

    # Bar 3 - Dissonant cluster with chromatic motion
    bar_3_notes = [
        (60, 2.0, 60),   # C
        (63, 2.0, 70),   # E♭
        (65, 2.0, 75),   # G
        (68, 2.0, 65),   # B♭
        (70, 2.0, 60),   # B
    ]

    # Bar 4 - A7 (G - E - C# - A)
    bar_4_notes = [
        (67, 3.0, 90),   # A
        (69, 3.0, 85),   # B
        (64, 3.0, 80),   # D
        (65, 3.0, 85),   # G
        (69, 3.0, 80),   # B (resting tone)
    ]

    def add_notes(notes):
        for pitch, time, velocity in notes:
            note = Note(pitch, velocity, time, time + 0.25)
            instrument.notes.append(note)

    add_notes(bar_1_notes)
    add_notes(bar_2_notes)
    add_notes(bar_3_notes)
    add_notes(bar_4_notes)

add_piano(piano_instrument, bar_times)

# -------------------
# SAX: Dante
# -------------------

def add_sax(instrument, bar_times):
    # Your melody: sparse, expressive, with space
    # Bar 1: Mysterious question
    # Bar 2: Tension builds
    # Bar 3: Glimmer of resolution
    # Bar 4: Lingering question

    # Bar 1: F, A, rest, Bb (soft, distant)
    # Bar 2: F, rest, G, A (tension builds)
    # Bar 3: Bb, rest, C, D (resolution glimmer)
    # Bar 4: E, rest, F, rest (lingering question)

    # Notes in F major: F (65), G (67), A (69), Bb (68), C (72), D (74), E (76)
    bar_1_notes = [
        (65, 0.0, 60),   # F (soft)
        (69, 0.5, 70),   # A
        (68, 1.0, 60),   # Bb
    ]

    bar_2_notes = [
        (65, 1.0, 70),   # F
        (67, 1.5, 75),   # G
        (69, 2.0, 70),   # A
    ]

    bar_3_notes = [
        (68, 2.0, 80),   # Bb
        (72, 2.5, 85),   # C
        (74, 3.0, 80),   # D
    ]

    bar_4_notes = [
        (76, 3.0, 65),   # E (lingering question)
        (65, 3.5, 60),   # F (soft)
    ]

    def add_notes(notes):
        for pitch, time, velocity in notes:
            note = Note(pitch, velocity, time, time + 0.25)
            instrument.notes.append(note)

    add_notes(bar_1_notes)
    add_notes(bar_2_notes)
    add_notes(bar_3_notes)
    add_notes(bar_4_notes)

add_sax(sax_instrument, bar_times)

# Save the MIDI file
pm.write("waynes_question.mid")
print("MIDI file generated: 'waynes_question.mid'")
