
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Track for each instrument
bass_track = pretty_midi.Track(program=33)  # Electric Bass
piano_track = pretty_midi.Track(program=0)  # Acoustic Piano
drums_track = pretty_midi.Track(program=11)  # Drum Kit
sax_track = pretty_midi.Track(program=64)  # Tenor Saxophone

pm.instruments.append(bass_track)
pm.instruments.append(piano_track)
pm.instruments.append(drums_track)
pm.instruments.append(sax_track)

# Time per beat (in seconds), at 160 BPM
beat = 60 / 160  # 0.375 seconds
bar = 4 * beat  # 1.5 seconds

# Bar 1: Little Ray (Drums) - 4/4 time
drum_notes = [
    # Kick on 1 and 3
    (pretty_midi.note_number_to_name(36), 0, 0.375),  # Kick on 1
    (pretty_midi.note_number_to_name(36), 1.125, 0.375),  # Kick on 3
    # Snare on 2 and 4
    (pretty_midi.note_number_to_name(38), 0.75, 0.375),  # Snare on 2
    (pretty_midi.note_number_to_name(38), 1.5, 0.375),  # Snare on 4
    # Hi-hat on every eighth
    (pretty_midi.note_number_to_name(42), 0, 0.1875),  # 1
    (pretty_midi.note_number_to_name(42), 0.1875, 0.1875),  # &1
    (pretty_midi.note_number_to_name(42), 0.375, 0.1875),  # 2
    (pretty_midi.note_number_to_name(42), 0.5625, 0.1875),  # &2
    (pretty_midi.note_number_to_name(42), 0.75, 0.1875),  # 3
    (pretty_midi.note_number_to_name(42), 0.9375, 0.1875),  # &3
    (pretty_midi.note_number_to_name(42), 1.125, 0.1875),  # 4
    (pretty_midi.note_number_to_name(42), 1.3125, 0.1875),  # &4
]

for note, start, duration in drum_notes:
    note_number = pretty_midi.note_name_to_number(note)
    drum_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums_track.notes.append(drum_note)

# Bar 1: Bass (Marcus) - Root and 5th with chromatic approach, Dm
# D (D2), F (F2), A (A2)
# Chromatic approach to D from C# (C#2)
# Beat 1: C#2, D2
# Beat 2: F2
# Beat 3: A2
# Beat 4: F2 (chromatic approach to D again)

bass_notes = [
    (pretty_midi.note_number_to_name(38), 0, 0.375),  # C#2
    (pretty_midi.note_number_to_name(39), 0, 0.375),  # D2
    (pretty_midi.note_number_to_name(41), 0.75, 0.375),  # F2
    (pretty_midi.note_number_to_name(44), 1.125, 0.375),  # A2
    (pretty_midi.note_number_to_name(41), 1.5, 0.375),  # F2
]

for note, start, duration in bass_notes:
    note_number = pretty_midi.note_name_to_name_to_number(note)
    bass_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass_track.notes.append(bass_note)

# Bar 1: Piano (Diane) - Open voicings, one chord, resolve on beat 4
# Dm7 (D, F, A, C) - open voicing, left hand
# Root (D2), 7th (C2), 5th (A2), 3rd (F2)

piano_notes = [
    (pretty_midi.note_number_to_name(39), 0, 0.1875),  # D2
    (pretty_midi.note_number_to_name(36), 0, 0.1875),  # C2
    (pretty_midi.note_number_to_name(44), 0, 0.1875),  # A2
    (pretty_midi.note_number_to_name(41), 0, 0.1875),  # F2
]

for note, start, duration in piano_notes:
    note_number = pretty_midi.note_name_to_number(note)
    piano_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano_track.notes.append(piano_note)

# Bar 2: Sax (Dante) - Melody: Dm (D, F, A, C) - short motif, starts on D2 (beat 1)
# D2 (beat 1) -> F2 (beat 2) -> A2 (beat 3) -> leave it hanging on beat 4
# No scale runs, just the motif

sax_notes = [
    (pretty_midi.note_number_to_name(39), 1.5, 0.375),  # D2 on beat 1
    (pretty_midi.note_number_to_name(41), 1.875, 0.375),  # F2 on beat 2
    (pretty_midi.note_number_to_name(44), 2.25, 0.375),  # A2 on beat 3
    # Beat 4: leave it hanging
]

for note, start, duration in sax_notes:
    note_number = pretty_midi.note_name_to_number(note)
    sax_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax_track.notes.append(sax_note)

# Bar 2: Bass - Walking line in Dm (D2-G2), roots and fifths with chromatic approach
# D (beat 1), F (beat 2), A (beat 3), C (beat 4)

bass_notes = [
    (pretty_midi.note_number_to_name(39), 1.5, 0.375),  # D2
    (pretty_midi.note_number_to_name(41), 1.875, 0.375),  # F2
    (pretty_midi.note_number_to_name(44), 2.25, 0.375),  # A2
    (pretty_midi.note_number_to_name(40), 2.625, 0.375),  # C2 (chromatic approach to D)
]

for note, start, duration in bass_notes:
    note_number = pretty_midi.note_name_to_number(note)
    bass_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass_track.notes.append(bass_note)

# Bar 2: Piano - Dm7, G7, C7, F7 (each bar with open voicings, resolve on the last beat)

# Bar 2: Dm7
piano_notes = [
    (pretty_midi.note_number_to_name(39), 1.5, 0.1875),  # D2
    (pretty_midi.note_number_to_name(41), 1.5, 0.1875),  # F2
    (pretty_midi.note_number_to_name(44), 1.5, 0.1875),  # A2
    (pretty_midi.note_number_to_name(36), 1.5, 0.1875),  # C2
]

for note, start, duration in piano_notes:
    note_number = pretty_midi.note_name_to_number(note)
    piano_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano_track.notes.append(piano_note)

# Bar 3: G7
piano_notes = [
    (pretty_midi.note_number_to_name(43), 2.25, 0.1875),  # G2
    (pretty_midi.note_number_to_name(45), 2.25, 0.1875),  # B2
    (pretty_midi.note_number_to_name(47), 2.25, 0.1875),  # D3
    (pretty_midi.note_number_to_name(40), 2.25, 0.1875),  # F2
]

for note, start, duration in piano_notes:
    note_number = pretty_midi.note_name_to_number(note)
    piano_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano_track.notes.append(piano_note)

# Bar 4: C7
piano_notes = [
    (pretty_midi.note_number_to_name(48), 3, 0.1875),  # C3
    (pretty_midi.note_number_to_name(50), 3, 0.1875),  # E3
    (pretty_midi.note_number_to_name(52), 3, 0.1875),  # G3
    (pretty_midi.note_number_to_name(44), 3, 0.1875),  # A2
]

for note, start, duration in piano_notes:
    note_number = pretty_midi.note_name_to_number(note)
    piano_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano_track.notes.append(piano_note)

# Bar 4: Drum Fill - Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth

drum_notes = [
    # Kick on 1 and 3
    (pretty_midi.note_number_to_name(36), 3, 0.375),  # Kick on 1
    (pretty_midi.note_number_to_name(36), 3.375, 0.375),  # Kick on 3
    # Snare on 2 and 4
    (pretty_midi.note_number_to_name(38), 3.75, 0.375),  # Snare on 2
    (pretty_midi.note_number_to_name(38), 4.125, 0.375),  # Snare on 4
    # Hi-hat on every eighth
    (pretty_midi.note_number_to_name(42), 3, 0.1875),  # 1
    (pretty_midi.note_number_to_name(42), 3.1875, 0.1875),  # &1
    (pretty_midi.note_number_to_name(42), 3.375, 0.1875),  # 2
    (pretty_midi.note_number_to_name(42), 3.5625, 0.1875),  # &2
    (pretty_midi.note_number_to_name(42), 3.75, 0.1875),  # 3
    (pretty_midi.note_number_to_name(42), 3.9375, 0.1875),  # &3
    (pretty_midi.note_number_to_name(42), 4.125, 0.1875),  # 4
    (pretty_midi.note_number_to_name(42), 4.3125, 0.1875),  # &4
]

for note, start, duration in drum_notes:
    note_number = pretty_midi.note_name_to_number(note)
    drum_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums_track.notes.append(drum_note)

# Bar 4: Bass - Walking line in Dm (D2-G2), roots and fifths with chromatic approach

bass_notes = [
    (pretty_midi.note_number_to_name(39), 3, 0.375),  # D2
    (pretty_midi.note_number_to_name(41), 3.375, 0.375),  # F2
    (pretty_midi.note_number_to_name(44), 3.75, 0.375),  # A2
    (pretty_midi.note_number_to_name(40), 4.125, 0.375),  # C2
]

for note, start, duration in bass_notes:
    note_number = pretty_midi.note_name_to_number(note)
    bass_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass_track.notes.append(bass_note)

# Bar 4: Sax - Repeat motif, resolve on A2 (beat 3), leave it hanging on beat 4

sax_notes = [
    (pretty_midi.note_number_to_name(39), 3, 0.375),  # D2 on beat 1
    (pretty_midi.note_number_to_name(41), 3.375, 0.375),  # F2 on beat 2
    (pretty_midi.note_number_to_name(44), 3.75, 0.375),  # A2 on beat 3
]

for note, start, duration in sax_notes:
    note_number = pretty_midi.note_name_to_number(note)
    sax_note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax_track.notes.append(sax_note)

# Save the MIDI file
pm.write("dante_intro.mid")
