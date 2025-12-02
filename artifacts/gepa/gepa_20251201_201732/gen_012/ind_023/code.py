
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key (D major)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0)]  # D major

# Define the instruments
# 1. Drums (Little Ray)
# 2. Bass (Marcus)
# 3. Piano (Diane)
# 4. Tenor Sax (You)

# Drums - Little Ray
drums = pretty_midi.Instrument(program=10)  # Drums
pm.instruments.append(drums)

# Bass - Marcus
bass = pretty_midi.Instrument(program=33)  # Double Bass
pm.instruments.append(bass)

# Piano - Diane
piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
pm.instruments.append(piano)

# Tenor Sax - You
sax = pretty_midi.Instrument(program=64)  # Tenor Sax
pm.instruments.append(sax)

# Utility: Convert beat to seconds (160 BPM)
def beat_to_time(beat):
    return beat / (160 / 60)

# Bar 1: Little Ray (drums) alone — setup
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in [0, 2]:  # Kick on 1 and 3
        kick = pretty_midi.Note(
            velocity=100,
            pitch=36,  # Kick
            start=beat_to_time(beat),
            end=beat_to_time(beat) + 0.1
        )
        drums.notes.append(kick)

    for beat in [1, 3]:  # Snare on 2 and 4
        snare = pretty_midi.Note(
            velocity=100,
            pitch=38,  # Snare
            start=beat_to_time(beat),
            end=beat_to_time(beat) + 0.1
        )
        drums.notes.append(snare)

    for beat in range(4):  # Hihat on every eighth
        for eighth in [0, 0.5]:
            hihat = pretty_midi.Note(
                velocity=80,
                pitch=42,  # Hihat
                start=beat_to_time(beat) + eighth,
                end=beat_to_time(beat) + eighth + 0.05
            )
            drums.notes.append(hihat)

# Bar 2: Full band in — Diane on piano, Marcus on bass, you on sax

# Diane on piano — open voicings, chord each bar
# Bar 2: Dmaj7 (root position)
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=beat_to_time(1), end=beat_to_time(1) + 0.5),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=beat_to_time(1), end=beat_to_time(1) + 0.5),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=beat_to_time(1), end=beat_to_time(1) + 0.5),  # B
    pretty_midi.Note(velocity=100, pitch=82, start=beat_to_time(1), end=beat_to_time(1) + 0.5)   # D
]
piano.notes.extend(diane_notes)

# Marcus on bass — walking line: D2, F#, A, B, D
bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat_to_time(1), end=beat_to_time(1) + 0.3))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=41, start=beat_to_time(1) + 0.3, end=beat_to_time(1) + 0.6))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=45, start=beat_to_time(1) + 0.6, end=beat_to_time(1) + 0.9))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=46, start=beat_to_time(1) + 0.9, end=beat_to_time(1) + 1.2))
bass.notes.extend(bass_notes)

# Your sax line — short motif, one phrase, leave it hanging
# Motif: D (62) -> F# (66) -> B (71) -> D (62) — syncopated, open-ended
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=beat_to_time(1), end=beat_to_time(1) + 0.3),
    pretty_midi.Note(velocity=110, pitch=66, start=beat_to_time(1) + 0.3, end=beat_to_time(1) + 0.6),
    pretty_midi.Note(velocity=110, pitch=71, start=beat_to_time(1) + 0.6, end=beat_to_time(1) + 0.9),
    pretty_midi.Note(velocity=110, pitch=62, start=beat_to_time(1) + 0.9, end=beat_to_time(1) + 1.2)
]
sax.notes.extend(sax_notes)

# Bar 3: Diane on piano (new chord: G7)
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=beat_to_time(2), end=beat_to_time(2) + 0.5),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=beat_to_time(2), end=beat_to_time(2) + 0.5),  # B
    pretty_midi.Note(velocity=100, pitch=81, start=beat_to_time(2), end=beat_to_time(2) + 0.5),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=beat_to_time(2), end=beat_to_time(2) + 0.5)   # F#
]
piano.notes.extend(diane_notes)

# Marcus on bass: G (45), B (49), D (52), F# (54)
bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=100, pitch=45, start=beat_to_time(2), end=beat_to_time(2) + 0.3))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=49, start=beat_to_time(2) + 0.3, end=beat_to_time(2) + 0.6))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=52, start=beat_to_time(2) + 0.6, end=beat_to_time(2) + 0.9))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=54, start=beat_to_time(2) + 0.9, end=beat_to_time(2) + 1.2))
bass.notes.extend(bass_notes)

# Bar 4: Diane on piano (new chord: A7)
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=beat_to_time(3), end=beat_to_time(3) + 0.5),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=beat_to_time(3), end=beat_to_time(3) + 0.5),  # C#
    pretty_midi.Note(velocity=100, pitch=83, start=beat_to_time(3), end=beat_to_time(3) + 0.5),  # E
    pretty_midi.Note(velocity=100, pitch=81, start=beat_to_time(3), end=beat_to_time(3) + 0.5)   # G
]
piano.notes.extend(diane_notes)

# Marcus on bass: A (55), C# (58), E (62), G (65)
bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=100, pitch=55, start=beat_to_time(3), end=beat_to_time(3) + 0.3))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=58, start=beat_to_time(3) + 0.3, end=beat_to_time(3) + 0.6))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=beat_to_time(3) + 0.6, end=beat_to_time(3) + 0.9))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=beat_to_time(3) + 0.9, end=beat_to_time(3) + 1.2))
bass.notes.extend(bass_notes)

# End of Bar 4 — leave sax hanging — don't resolve
# No resolution, just the motif again, but shorter, more open
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=beat_to_time(3), end=beat_to_time(3) + 0.2),
    pretty_midi.Note(velocity=110, pitch=66, start=beat_to_time(3) + 0.2, end=beat_to_time(3) + 0.4),
    pretty_midi.Note(velocity=110, pitch=71, start=beat_to_time(3) + 0.4, end=beat_to_time(3) + 0.6),
]
sax.notes.extend(sax_notes)

# Save the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file 'jazz_intro.mid' has been created.")
