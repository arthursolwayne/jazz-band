
import pretty_midi

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.instruments = []

# Constants
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = BEAT * 4    # seconds per bar
TICKS_PER_BEAT = 960  # 960 ticks per beat for higher resolution
TICKS_PER_BAR = TICKS_PER_BEAT * 4

# Define MIDI note values
D2 = 38  # D2 (MIDI note)
G2 = 43  # G2
C3 = 48  # C3
F3 = 53  # F3
Bb3 = 55 # Bb3
B3 = 57  # B3
E4 = 64  # E4
A4 = 69  # A4
D4 = 62  # D4
F4 = 65  # F4
G4 = 67  # G4
B4 = 71  # B4
C5 = 72  # C5
E5 = 76  # E5

# Bass (Marcus)
bass = pretty_midi.Instrument(program=33)  # Double Bass
pm.instruments.append(bass)

# Drum (Little Ray)
drums = pretty_midi.Instrument(program=0)  # Acoustic Drum Set
pm.instruments.append(drums)

# Piano (Diane)
piano = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano
pm.instruments.append(piano)

# Tenor Sax (Dante)
sax = pretty_midi.Instrument(program=64)  # Tenor Saxophone
pm.instruments.append(sax)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for tick in range(0, TICKS_PER_BAR, TICKS_PER_BEAT // 2):
    if tick % (TICKS_PER_BEAT // 2) == 0:
        # Kick on 1 and 3
        if tick % TICKS_PER_BEAT == 0 or tick % TICKS_PER_BEAT == TICKS_PER_BEAT // 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=tick / TICKS_PER_BEAT, end=(tick + 20) / TICKS_PER_BEAT)
            drums.notes.append(note)
        # Snare on 2 and 4
        if tick % TICKS_PER_BEAT == TICKS_PER_BEAT // 4 or tick % TICKS_PER_BEAT == TICKS_PER_BEAT * 3 // 4:
            note = pretty_midi.Note(velocity=100, pitch=38, start=tick / TICKS_PER_BEAT, end=(tick + 20) / TICKS_PER_BEAT)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=tick / TICKS_PER_BEAT, end=(tick + 10) / TICKS_PER_BEAT)
        drums.notes.append(note)

# Bar 2: All instruments in
# Piano (Diane): Open voicings, different chord each bar
piano_notes = [
    # Bar 2: D7 (D F# A C#) open voicing
    (D4, 0.0), (F4, 0.0), (A4, 0.0), (C5, 0.0),
    # Bar 3: G7 (G B D F) open voicing
    (G4, 1.5), (B4, 1.5), (D5, 1.5), (F5, 1.5),
    # Bar 4: Bb7 (Bb D F Ab) open voicing
    (Bb3, 3.0), (D4, 3.0), (F4, 3.0), (Ab4, 3.0)
]
for pitch, start in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 1.5)
    piano.notes.append(note)

# Bass (Marcus): Walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 -> Eb2 -> G2
    (D2, 0.0, 0.5), (E2, 0.5, 0.75), (G2, 0.75, 1.5),
    # Bar 3: G2 -> Ab2 -> Bb2 -> B2
    (G2, 1.5, 2.0), (Ab2, 2.0, 2.25), (Bb2, 2.25, 2.75), (B2, 2.75, 3.0),
    # Bar 4: B2 -> C3 -> D3 -> F3
    (B2, 3.0, 3.5), (C3, 3.5, 3.75), (D3, 3.75, 4.25), (F3, 4.25, 4.5)
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * BAR
    for tick in range(0, TICKS_PER_BAR, TICKS_PER_BEAT // 2):
        if tick % (TICKS_PER_BEAT // 2) == 0:
            # Kick on 1 and 3
            if tick % TICKS_PER_BEAT == 0 or tick % TICKS_PER_BEAT == TICKS_PER_BEAT // 2:
                note = pretty_midi.Note(velocity=100, pitch=36, start=start + tick / TICKS_PER_BEAT, end=start + (tick + 20) / TICKS_PER_BEAT)
                drums.notes.append(note)
            # Snare on 2 and 4
            if tick % TICKS_PER_BEAT == TICKS_PER_BEAT // 4 or tick % TICKS_PER_BEAT == TICKS_PER_BEAT * 3 // 4:
                note = pretty_midi.Note(velocity=100, pitch=38, start=start + tick / TICKS_PER_BEAT, end=start + (tick + 20) / TICKS_PER_BEAT)
                drums.notes.append(note)
            # Hi-hat on every eighth
            note = pretty_midi.Note(velocity=80, pitch=42, start=start + tick / TICKS_PER_BEAT, end=start + (tick + 10) / TICKS_PER_BEAT)
            drums.notes.append(note)

# Saxophone (Dante): One short motif, make it sing
# Start at bar 2, 0.0 seconds
# Motif: D4 -> Eb4 -> F4 -> D4 (sings, leaves it hanging)
sax_notes = [
    (D4, 0.0, 0.75),  # Start with D4
    (E4, 0.75, 1.25), # Chromatic approach to F4 (the question)
    (F4, 1.25, 1.5)   # Hit the resolution, then leave it hanging
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")
