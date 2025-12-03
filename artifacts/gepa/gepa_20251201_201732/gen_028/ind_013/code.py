
import pretty_midi

# Create a PrettyMIDI object with 160 BPM and 4/4 time
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: Fm (F minor)
key = 'Fm'

# Define instrument tracks
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create tracks
bass_track = pretty_midi.Instrument(program=bass_program)
piano_track = pretty_midi.Instrument(program=piano_program)
drums_track = pretty_midi.Instrument(program=drums_program)
sax_track = pretty_midi.Instrument(program=sax_program)

# Add tracks to the PrettyMIDI object
pm.instruments = [bass_track, piano_track, drums_track, sax_track]

# Define timing parameters
BPM = 160
beats_per_bar = 4
beat_duration = 60.0 / BPM  # seconds per beat
bar_duration = beats_per_bar * beat_duration  # 6 seconds per bar

# Time values for each bar
times = [0.0, bar_duration, 2 * bar_duration, 3 * bar_duration]

### DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(4):
    for beat in range(4):
        time = bar * bar_duration + beat * beat_duration

        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            kick = pretty_midi.Note(
                velocity=100,
                pitch=36,  # Kick
                start=time,
                end=time + 0.1
            )
            drums_track.notes.append(kick)

        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            snare = pretty_midi.Note(
                velocity=90,
                pitch=38,  # Snare
                start=time,
                end=time + 0.08
            )
            drums_track.notes.append(snare)

        # Hihat on every eighth
        for subbeat in range(2):
            hihat_time = time + subbeat * (beat_duration / 2)
            hihat = pretty_midi.Note(
                velocity=70,
                pitch=42,  # Hihat
                start=hihat_time,
                end=hihat_time + 0.02
            )
            drums_track.notes.append(hihat)

### BASS: Marcus (Walking line - Roots and fifths with chromatic approaches)

# Define bass notes in Fm (F, Ab, Bb, C, D, Eb, F)
# Root and fifth with chromatic approaches

bass_notes = [
    # Bar 1: F (root) -> Ab (fifth) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=53, start=0.0, end=0.375),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=0.375, end=0.75),  # E
    pretty_midi.Note(velocity=80, pitch=52, start=0.75, end=1.125),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=1.125, end=1.5),  # Ab

    # Bar 2: Bb (fifth of Ab) -> C (root of Bb)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),  # C

    # Bar 3: D (fifth of C) -> Eb (fifth of D)
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # Eb

    # Bar 4: F (root) -> Ab (fifth) again, resolving with a chromatic approach
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0),  # Ab
]

bass_track.notes.extend(bass_notes)

### PIANO: Diane (Open voicings, different chord each bar, resolve on the last)

# Bar 1: Fm7 (F, Ab, C, Eb)
# Bar 2: Bb7 (Bb, D, F, Ab)
# Bar 3: C7 (C, E, G, Bb)
# Bar 4: Eb7 (Eb, G, Bb, D)

# Define the chords as open voicings (root, 3rd, 5th, 7th)
# Comp on 2 and 4 (beat 1 and 3 are rests)

chord_notes = []

# Bar 1: Fm7 (F, Ab, C, Eb)
chord_notes.extend([
    pretty_midi.Note(velocity=85, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=85, pitch=57, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=85, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=1.875),  # Eb
])

# Bar 2: Bb7 (Bb, D, F, Ab)
chord_notes.extend([
    pretty_midi.Note(velocity=85, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=85, pitch=52, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=85, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=85, pitch=57, start=3.0, end=3.375),  # Ab
])

# Bar 3: C7 (C, E, G, Bb)
chord_notes.extend([
    pretty_midi.Note(velocity=85, pitch=55, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=85, pitch=57, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=85, pitch=59, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=85, pitch=50, start=4.5, end=4.875),  # Bb
])

# Bar 4: Eb7 (Eb, G, Bb, D)
chord_notes.extend([
    pretty_midi.Note(velocity=85, pitch=60, start=6.0, end=6.375),  # Eb
    pretty_midi.Note(velocity=85, pitch=62, start=6.0, end=6.375),  # G
    pretty_midi.Note(velocity=85, pitch=50, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=85, pitch=52, start=6.0, end=6.375),  # D
])

piano_track.notes.extend(chord_notes)

### SAX: You (Tenor Sax) — Short motif that sings and leaves a question

# Motif: F (53) -> Gb (54) -> Ab (57) -> F (53) — a descending triplet with a chromatic approach

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=54, start=0.0, end=1.5),  # F (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=3.0),  # Gb
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=6.0),  # F (resolution)
]

sax_track.notes.extend(sax_notes)

# Save the MIDI file
pm.write("waynes_intro.mid")
print("MIDI file saved as 'waynes_intro.mid'")
