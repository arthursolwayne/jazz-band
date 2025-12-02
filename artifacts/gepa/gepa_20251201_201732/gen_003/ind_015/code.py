
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Create instruments
bass_instrument = Instrument(program=33)  # Electric Bass
piano_instrument = Instrument(program=0)  # Acoustic Piano
drums_instrument = Instrument(program=0)  # Drums
sax_instrument = Instrument(program=64)  # Tenor Saxophone

pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# Ticks per beat (assuming 480 ticks per beat is standard)
ticks_per_beat = 480
bar_length_ticks = ticks_per_beat * 4  # 4/4 time, 4 bars = 16 beats, but we only use 4 bars (6 seconds at 160 BPM)

# BAR 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            drums_instrument.notes.append(Note(36, 60, bar * ticks_per_beat + beat * ticks_per_beat, bar * ticks_per_beat + beat * ticks_per_beat + 30))
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            drums_instrument.notes.append(Note(38, 60, bar * ticks_per_beat + beat * ticks_per_beat, bar * ticks_per_beat + beat * ticks_per_beat + 30))
        for eighth in range(2):
            # Hihat on every eighth
            drums_instrument.notes.append(Note(42, 60, bar * ticks_per_beat + beat * ticks_per_beat + eighth * ticks_per_beat // 2, bar * ticks_per_beat + beat * ticks_per_beat + eighth * ticks_per_beat // 2 + 10))

# BAR 2: Everyone in. Bass enters with walking line, piano with open voicings, sax with motif

# Marcus: Bass (D2 to G2, roots and fifths with chromatic approaches)
# Root: D2 (MIDI 38), fifth: A2 (MIDI 43)
# Chromatic approaches: C#2 (37), A#2 (44)
bass_notes = [
    Note(38, 60, 1 * ticks_per_beat, 1 * ticks_per_beat + 30),  # D2, beat 1
    Note(37, 60, 1 * ticks_per_beat + ticks_per_beat // 2, 1 * ticks_per_beat + ticks_per_beat // 2 + 30),  # C#2, beat 2
    Note(43, 60, 1 * ticks_per_beat + ticks_per_beat, 1 * ticks_per_beat + ticks_per_beat + 30),  # A2, beat 3
    Note(44, 60, 1 * ticks_per_beat + ticks_per_beat * 1.5, 1 * ticks_per_beat + ticks_per_beat * 1.5 + 30),  # A#2, beat 4
]
bass_instrument.notes.extend(bass_notes)

# Diane: Piano, open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
# Bar 2: Open voicing on 2 and 4
# Dm7: D (62), F (65), A (69), C (60)
# Dm7 -> C (60) on 2 and 4
diane_notes_bar2 = [
    Note(62, 60, 1 * ticks_per_beat + ticks_per_beat // 2, 1 * ticks_per_beat + ticks_per_beat // 2 + 60),  # D
    Note(65, 60, 1 * ticks_per_beat + ticks_per_beat // 2, 1 * ticks_per_beat + ticks_per_beat // 2 + 60),  # F
    Note(69, 60, 1 * ticks_per_beat + ticks_per_beat // 2, 1 * ticks_per_beat + ticks_per_beat // 2 + 60),  # A
    Note(60, 60, 1 * ticks_per_beat + ticks_per_beat // 2, 1 * ticks_per_beat + ticks_per_beat // 2 + 60),  # C
]
diane_notes_bar3 = [
    Note(67, 60, 1 * ticks_per_beat + ticks_per_beat * 1.5, 1 * ticks_per_beat + ticks_per_beat * 1.5 + 60),  # G
    Note(62, 60, 1 * ticks_per_beat + ticks_per_beat * 1.5, 1 * ticks_per_beat + ticks_per_beat * 1.5 + 60),  # Bb
    Note(69, 60, 1 * ticks_per_beat + ticks_per_beat * 1.5, 1 * ticks_per_beat + ticks_per_beat * 1.5 + 60),  # D
    Note(65, 60, 1 * ticks_per_beat + ticks_per_beat * 1.5, 1 * ticks_per_beat + ticks_per_beat * 1.5 + 60),  # F
]
diane_notes_bar4 = [
    Note(60, 60, 1 * ticks_per_beat + ticks_per_beat * 2.5, 1 * ticks_per_beat + ticks_per_beat * 2.5 + 60),  # C
    Note(64, 60, 1 * ticks_per_beat + ticks_per_beat * 2.5, 1 * ticks_per_beat + ticks_per_beat * 2.5 + 60),  # Eb
    Note(67, 60, 1 * ticks_per_beat + ticks_per_beat * 2.5, 1 * ticks_per_beat + ticks_per_beat * 2.5 + 60),  # G
    Note(62, 60, 1 * ticks_per_beat + ticks_per_beat * 2.5, 1 * ticks_per_beat + ticks_per_beat * 2.5 + 60),  # Bb
]
piano_instrument.notes.extend(diane_notes_bar2)
piano_instrument.notes.extend(diane_notes_bar3)
piano_instrument.notes.extend(diane_notes_bar4)

# Little Ray: Keep the same pattern in bars 2-4
for bar in range(1, 4):
    for beat in range(4):
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            drums_instrument.notes.append(Note(36, 60, bar * ticks_per_beat + beat * ticks_per_beat, bar * ticks_per_beat + beat * ticks_per_beat + 30))
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            drums_instrument.notes.append(Note(38, 60, bar * ticks_per_beat + beat * ticks_per_beat, bar * ticks_per_beat + beat * ticks_per_beat + 30))
        for eighth in range(2):
            # Hihat on every eighth
            drums_instrument.notes.append(Note(42, 60, bar * ticks_per_beat + beat * ticks_per_beat + eighth * ticks_per_beat // 2, bar * ticks_per_beat + beat * ticks_per_beat + eighth * ticks_per_beat // 2 + 10))

# BAR 2: You on sax — short motif, one phrase, start it, leave it hanging, come back to finish

# Motif: Dm scale fragment — D (62), E (64), F (65), G (67), A (69) — but not all at once, just a whisper
# Use rests and space to let the phrase breathe

# First note: D (62) on beat 1
sax_notes = [
    Note(62, 80, 1 * ticks_per_beat, 1 * ticks_per_beat + 90),  # D
    Note(64, 80, 1 * ticks_per_beat + ticks_per_beat // 2, 1 * ticks_per_beat + ticks_per_beat // 2 + 90),  # E
    Note(65, 80, 1 * ticks_per_beat + ticks_per_beat, 1 * ticks_per_beat + ticks_per_beat + 90),  # F
    Note(67, 80, 1 * ticks_per_beat + ticks_per_beat * 1.5, 1 * ticks_per_beat + ticks_per_beat * 1.5 + 90),  # G
    Note(69, 80, 1 * ticks_per_beat + ticks_per_beat * 2.5, 1 * ticks_per_beat + ticks_per_beat * 2.5 + 90),  # A (resolution)
]
sax_instrument.notes.extend(sax_notes)

# Save the MIDI file
pm.write("dante_intro.mid")
