
import pretty_midi
import numpy as np

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature to D minor (no accidentals)
midi.key_signature_changes = [pretty_midi.KeySignature(2, 0)]  # 2 = D minor

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Double Bass
piano = pretty_midi.Instrument(program=0)   # Acoustic Piano
sax = pretty_midi.Instrument(program=64)    # Tenor Saxophone

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Define the beat length (in seconds)
beat = 60 / 160  # 60 seconds per minute / 160 beats per minute
bar_length = 4 * beat  # 4 beats per bar

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth

# Define the timing for each beat
def add_drums():
    for bar in range(4):
        for beat in [0, 2]:  # Kick on 1 and 3
            kick_time = bar * bar_length + beat * beat
            kick = pretty_midi.Note(
                velocity=100,
                pitch=36,  # Kick drum
                start=kick_time,
                end=kick_time + 0.1
            )
            drums.notes.append(kick)

        for beat in [1, 3]:  # Snare on 2 and 4
            snare_time = bar * bar_length + beat * beat
            snare = pretty_midi.Note(
                velocity=100,
                pitch=38,  # Snare drum
                start=snare_time,
                end=snare_time + 0.1
            )
            drums.notes.append(snare)

        for eighth in range(8):  # Hi-hat on every eighth
            hihat_time = bar * bar_length + eighth * (beat / 2)
            hihat = pretty_midi.Note(
                velocity=90,
                pitch=42,  # Hi-hat
                start=hihat_time,
                end=hihat_time + 0.05
            )
            drums.notes.append(hihat)

add_drums()

# --- BASS: Marcus ---
# Walking line, chromatic approaches, no repeated notes

def add_bass():
    # Bass line: Dm7 -> Gm7 -> Cm7 -> Fm7
    # Chromatic approach to each chord root

    # Dm7: D, F, A, C
    # Approach D with C#
    bass_notes = [
        (0, 3, 0.2),  # C# (D - 1 semitone)
        (0, 2, 0.2),  # D
        (0, 1, 0.2),  # F (from Gm7)
        (0, 3, 0.2),  # G
        (0, 2, 0.2),  # G
        (0, 1, 0.2),  # Bb (from Cm7)
        (0, 3, 0.2),  # C
        (0, 2, 0.2),  # C
        (0, 1, 0.2),  # Eb (from Fm7)
        (0, 3, 0.2),  # F
        (0, 2, 0.2),  # F
        (0, 1, 0.2),  # Ab
        (0, 3, 0.2),  # Bb
        (0, 2, 0.2),  # Bb
        (0, 1, 0.2),  # Db
        (0, 3, 0.2),  # D
    ]

    # Map MIDI notes (D = 62)
    root = 62
    notes = [pretty_midi.Note(
        velocity=90,
        pitch=root + note,
        start=i * beat,
        end=i * beat + duration
    ) for i, (velocity, note, duration) in enumerate(bass_notes)]

    bass.notes.extend(notes)

add_bass()

# --- PIANO: Diane ---
# 7th chords, comp on 2 and 4, out of the way

def add_piano():
    # Dm7: D F A C
    # Gm7: G Bb D F
    # Cm7: C Eb G Bb
    # Fm7: F Ab C Eb

    chords = [
        # Bar 1: Dm7 on 2 and 4
        (2 * beat, [62, 65, 69, 71], 0.5),
        (4 * beat, [62, 65, 69, 71], 0.5),
        # Bar 2: Gm7 on 2 and 4
        (6 * beat, [67, 70, 62, 65], 0.5),
        (8 * beat, [67, 70, 62, 65], 0.5),
        # Bar 3: Cm7 on 2 and 4
        (10 * beat, [60, 64, 67, 70], 0.5),
        (12 * beat, [60, 64, 67, 70], 0.5),
        # Bar 4: Fm7 on 2 and 4
        (14 * beat, [65, 68, 60, 64], 0.5),
        (16 * beat, [65, 68, 60, 64], 0.5),
    ]

    for start, pitches, duration in chords:
        for pitch in pitches:
            note = pretty_midi.Note(
                velocity=95,
                pitch=pitch,
                start=start,
                end=start + duration
            )
            piano.notes.append(note)

add_piano()

# --- SAX: Dante ---
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

def add_sax():
    # Motif: D -> F -> A -> C -> D
    # But with some tension, maybe a chromatic passing tone

    # Bar 1: Start the motif on the first beat
    notes = [
        (0, 62, 0.2),    # D
        (1, 63, 0.1),    # Eb (tension)
        (1, 65, 0.2),    # F
        (2, 69, 0.2),    # A
        (3, 71, 0.2),    # C
        (4, 62, 0.2),    # D
        (5, 62, 0.2),    # D (end of bar, unresolved)
    ]

    for beat, pitch, duration in notes:
        start = beat * beat
        note = pretty_midi.Note(
            velocity=110,
            pitch=pitch,
            start=start,
            end=start + duration
        )
        sax.notes.append(note)

add_sax()

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' has been created.")
