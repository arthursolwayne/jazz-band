
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature_changes.append(time_signature)

# Define instruments
# 1. Drums (Little Ray)
drums = Instrument(program=Program.DRUM_SET, is_drum=True)
pm.instruments.append(drums)

# 2. Bass (Marcus)
bass = Instrument(program=Program.BASS_GUITAR_FINGERSTYLE)
pm.instruments.append(bass)

# 3. Piano (Diane)
piano = Instrument(program=Program.ACOUSTIC_PIANO)
pm.instruments.append(piano)

# 4. Tenor Sax (You)
sax = Instrument(program=Program.SAXOPHONE_TENOR)
pm.instruments.append(sax)

# Time per bar (160 BPM, 4/4)
bar_length = 60.0 / 160 * 4  # 1.5 seconds per bar
note_length = bar_length / 8  # 0.1875 seconds per eighth note

# =============== BAR 1: DRUMS (Little Ray) ===============
# Bar 1: Rhythmic, space, not too busy
# Kick on 1, 3; snare on 2, 4; hihat on every eighth
# Add some fills on the offbeats

# Define MIDI note numbers for drums
kicks = [36]  # Kick
snares = [38]  # Snare
hihats = [42]  # Hi-hat
cymbals = [49]  # Crash cymbal

# Bar 1: Kick on 1, 3; snare on 2, 4; hihat on every eighth
bar1_start = 0.0
bar1_end = bar_length

# Kick on 1 and 3 (1st and 3rd beat)
drums.notes.append(Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.1))
drums.notes.append(Note(velocity=100, pitch=36, start=bar1_start + bar_length * 0.5, end=bar1_start + bar_length * 0.5 + 0.1))

# Snare on 2 and 4
drums.notes.append(Note(velocity=100, pitch=38, start=bar1_start + bar_length * 0.25, end=bar1_start + bar_length * 0.25 + 0.1))
drums.notes.append(Note(velocity=100, pitch=38, start=bar1_start + bar_length * 0.75, end=bar1_start + bar_length * 0.75 + 0.1))

# Hihat on every eighth
for i in range(8):
    start = bar1_start + note_length * i
    drums.notes.append(Note(velocity=80, pitch=42, start=start, end=start + 0.05))

# Crash cymbal at the end of bar 1 (a fill, to build tension)
drums.notes.append(Note(velocity=100, pitch=49, start=bar1_end - 0.2, end=bar1_end))

# =============== BAR 2: BASS (Marcus), PIANO (Diane), SAX (You) ===============

bar2_start = bar_length
bar2_end = 2 * bar_length

# ============ BASS: Chromatic walking line, with tension ============
# F major scale chromatic walking line (F, Gb, G, Ab, A, Bb, B, C)
# Playing around the key, not just walking forward
bass_notes = [
    (bar2_start, 70),  # F
    (bar2_start + note_length * 1.5, 69),  # Gb
    (bar2_start + note_length * 3, 71),  # G
    (bar2_start + note_length * 4.5, 68),  # Ab
    (bar2_start + note_length * 6, 72),  # A
    (bar2_start + note_length * 7.5, 70),  # Bb
    (bar2_start + note_length * 9, 71),  # B
    (bar2_start + note_length * 10.5, 72),  # C
]

for start, pitch in bass_notes:
    bass.notes.append(Note(velocity=90, pitch=pitch, start=start, end=start + 0.05))

# ============ PIANO: Aggressive 7th chords ============
# Diane plays 7th chords on 2 and 4, with a sense of direction
# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab

# Bar 2: F7 on 2 and 4
note_length_2 = bar_length / 2
piano_notes = [
    # 2nd beat
    (bar2_start + note_length_2, 71),  # F
    (bar2_start + note_length_2, 76),  # A
    (bar2_start + note_length_2, 77),  # C
    (bar2_start + note_length_2, 74),  # Eb
    # 4th beat
    (bar2_start + note_length_2 * 2, 70),  # Bb
    (bar2_start + note_length_2 * 2, 75),  # D
    (bar2_start + note_length_2 * 2, 77),  # F
    (bar2_start + note_length_2 * 2, 73),  # Ab
]

for start, pitch in piano_notes:
    piano.notes.append(Note(velocity=100, pitch=pitch, start=start, end=start + 0.1))

# ============ SAX: Simple, haunting motif ============
# F, Ab, Bb, C — a simple motif with a question at the end

sax_notes = [
    (bar2_start, 71),  # F
    (bar2_start + note_length * 1.5, 73),  # Ab
    (bar2_start + note_length * 3, 70),  # Bb
    (bar2_start + note_length * 4.5, 72),  # C
]

for start, pitch in sax_notes:
    sax.notes.append(Note(velocity=105, pitch=pitch, start=start, end=start + 0.1))

# =============== BAR 3: BASS, PIANO, SAX ===============

bar3_start = 2 * bar_length
bar3_end = 3 * bar_length

# ============ BASS: Continuing the chromatic line ============
# F, Gb, G, Ab, A, Bb, B, C, D, Eb, F
bass_notes = [
    (bar3_start, 70),  # F
    (bar3_start + note_length * 1.5, 69),  # Gb
    (bar3_start + note_length * 3, 71),  # G
    (bar3_start + note_length * 4.5, 68),  # Ab
    (bar3_start + note_length * 6, 72),  # A
    (bar3_start + note_length * 7.5, 70),  # Bb
    (bar3_start + note_length * 9, 71),  # B
    (bar3_start + note_length * 10.5, 72),  # C
    (bar3_start + note_length * 12, 74),  # D
    (bar3_start + note_length * 13.5, 71),  # Eb
    (bar3_start + note_length * 15, 70),  # F
]

for start, pitch in bass_notes:
    bass.notes.append(Note(velocity=90, pitch=pitch, start=start, end=start + 0.05))

# ============ PIANO: Moving chords with direction ============
# Bb7 on 2 and 4
note_length_2 = bar_length / 2
piano_notes = [
    # 2nd beat
    (bar3_start + note_length_2, 70),  # Bb
    (bar3_start + note_length_2, 75),  # D
    (bar3_start + note_length_2, 77),  # F
    (bar3_start + note_length_2, 73),  # Ab
    # 4th beat
    (bar3_start + note_length_2 * 2, 71),  # F
    (bar3_start + note_length_2 * 2, 76),  # A
    (bar3_start + note_length_2 * 2, 77),  # C
    (bar3_start + note_length_2 * 2, 74),  # Eb
]

for start, pitch in piano_notes:
    piano.notes.append(Note(velocity=100, pitch=pitch, start=start, end=start + 0.1))

# ============ SAX: Repeat motif, but with a twist ============
# F, Ab, Bb, C — same motif, but end on C with a long note to linger
sax_notes = [
    (bar3_start, 71),  # F
    (bar3_start + note_length * 1.5, 73),  # Ab
    (bar3_start + note_length * 3, 70),  # Bb
    (bar3_start + note_length * 4.5, 72),  # C
    (bar3_start + note_length * 4.5, 72),  # C (long note)
]

for start, pitch in sax_notes:
    sax.notes.append(Note(velocity=105, pitch=pitch, start=start, end=start + 0.1))

# =============== BAR 4: BASS, PIANO, SAX ===============

bar4_start = 3 * bar_length
bar4_end = 4 * bar_length

# ============ BASS: Continuing chromatic line ============
bass_notes = [
    (bar4_start, 70),  # F
    (bar4_start + note_length * 1.5, 69),  # Gb
    (bar4_start + note_length * 3, 71),  # G
    (bar4_start + note_length * 4.5, 68),  # Ab
    (bar4_start + note_length * 6, 72),  # A
    (bar4_start + note_length * 7.5, 70),  # Bb
    (bar4_start + note_length * 9, 71),  # B
    (bar4_start + note_length * 10.5, 72),  # C
    (bar4_start + note_length * 12, 74),  # D
    (bar4_start + note_length * 13.5, 71),  # Eb
    (bar4_start + note_length * 15, 70),  # F
]

for start, pitch in bass_notes:
    bass.notes.append(Note(velocity=90, pitch=pitch, start=start, end=start + 0.05))

# ============ PIANO: F7 on 2 and 4 ============
note_length_2 = bar_length / 2
piano_notes = [
    # 2nd beat
    (bar4_start + note_length_2, 71),  # F
    (bar4_start + note_length_2, 76),  # A
    (bar4_start + note_length_2, 77),  # C
    (bar4_start + note_length_2, 74),  # Eb
    # 4th beat
    (bar4_start + note_length_2 * 2, 70),  # Bb
    (bar4_start + note_length_2 * 2, 75),  # D
    (bar4_start + note_length_2 * 2, 77),  # F
    (bar4_start + note_length_2 * 2, 73),  # Ab
]

for start, pitch in piano_notes:
    piano.notes.append(Note(velocity=100, pitch=pitch, start=start, end=start + 0.1))

# ============ SAX: Repeat motif, but end on a sustaining note ============
# F, Ab, Bb, C — with the final C sustained for longer
sax_notes = [
    (bar4_start, 71),  # F
    (bar4_start + note_length * 1.5, 73),  # Ab
    (bar4_start + note_length * 3, 70),  # Bb
    (bar4_start + note_length * 4.5, 72),  # C
    (bar4_start + note_length * 4.5, 72),  # C (long note)
]

for start, pitch in sax_notes:
    sax.notes.append(Note(velocity=105, pitch=pitch, start=start, end=start + 0.1))

# Save the MIDI file
pm.write("jazz_intro_wayne.mid")
