
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up time signature (4/4)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes = [time_signature]

# Define key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# We'll use F minor scale: F, Gb, Ab, Bb, B, Db, Eb

# Define note durations and beats (in seconds)
beat = 0.375  # 160 BPM => 60/160 = 0.375s per beat
bar = 1.5     # 4 beats per bar

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)   # Upright Bass
piano = pretty_midi.Instrument(program=0)   # Acoustic Piano
sax = pretty_midi.Instrument(program=64)    # Tenor Sax

# ------------------ DRUMS: Little Ray ------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_idx in range(4):
    for beat_idx in range(4):
        time = bar_idx * bar + beat_idx * beat
        if beat_idx == 0 or beat_idx == 2:  # Kick on 1 & 3
            note = pretty_midi.Note(velocity=100, pitch=35, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat_idx == 1 or beat_idx == 3:  # Snare on 2 & 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth (add some variation in velocity)
        if beat_idx % 1 == 0:
            note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
            drums.notes.append(note)

# ------------------ BASS: Marcus ------------------
# Walking line in F minor: D2-G2, roots and fifths with chromatic approaches
# Bars 1-4: Fm7 -> Bbm7 -> Eb7 -> Am7 (no resolution in first 3 bars)
# Bass line: F, Ab, Bb, D, Gb, Bb, Db, F (chromatic approach to Bb)

bass_notes = [
    pretty_midi.Note(velocity=70, pitch=71, start=0, end=0.375),   # F2
    pretty_midi.Note(velocity=70, pitch=70, start=0.375, end=0.75), # Eb2
    pretty_midi.Note(velocity=70, pitch=69, start=0.75, end=1.125), # D2
    pretty_midi.Note(velocity=70, pitch=72, start=1.125, end=1.5),  # F2 (end of bar 1)

    pretty_midi.Note(velocity=70, pitch=67, start=1.5, end=1.875),  # Bb2
    pretty_midi.Note(velocity=70, pitch=68, start=1.875, end=2.25), # B2
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=70, pitch=66, start=2.625, end=3.0),  # Ab2 (end of bar 2)

    pretty_midi.Note(velocity=70, pitch=66, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=70, pitch=67, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=70, pitch=68, start=3.75, end=4.125), # B2
    pretty_midi.Note(velocity=70, pitch=70, start=4.125, end=4.5),  # Eb2 (end of bar 3)

    pretty_midi.Note(velocity=70, pitch=69, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=70, pitch=71, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=70, pitch=69, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=70, pitch=68, start=5.625, end=6.0),  # B2 (end of bar 4)
]

bass.notes = bass_notes

# ------------------ PIANO: Diane ------------------
# Open voicings, different chord each bar, resolve on the last
# Bar 1: Fm7 (F, Ab, Bb, Db)
# Bar 2: Bbm7 (Bb, Db, F, Ab)
# Bar 3: Eb7 (Eb, G, Bb, D)
# Bar 4: Am7 (A, C, Eb, G)

# Bar 1: Fm7 (F, Ab, Bb, Db) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=0, end=0.375),   # F4
    pretty_midi.Note(velocity=85, pitch=68, start=0, end=0.375),   # Ab4
    pretty_midi.Note(velocity=80, pitch=67, start=0, end=0.375),   # Bb4
    pretty_midi.Note(velocity=75, pitch=64, start=0, end=0.375),   # Db4

    # Bar 2: Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),  # Db4
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=75, pitch=68, start=1.5, end=1.875),  # Ab4

    # Bar 3: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Bb4 (same as G4, but different octave?) 
    pretty_midi.Note(velocity=75, pitch=62, start=3.0, end=3.375),  # D4

    # Bar 4: Am7 (A, C, Eb, G)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=85, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=75, pitch=67, start=4.5, end=4.875),  # G4
]

piano.notes = piano_notes

# ------------------ SAX: Dante Russo ------------------
# Short motif, concise, melodic, memorable
# Motif: F (beat 1), Bb (beat 2), Ab (beat 3), F (beat 4) — with a rest on beat 1 to start
# Then repeat with a slight variation in bar 4 to resolve

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=0.375, end=0.75),  # F4 (beat 2)
    pretty_midi.Note(velocity=100, pitch=67, start=0.75, end=1.125),  # Bb4 (beat 3)
    pretty_midi.Note(velocity=100, pitch=68, start=1.125, end=1.5),   # Ab4 (beat 4) — end of bar 1

    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),   # F4 (beat 1)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Bb4 (beat 2)
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab4 (beat 3)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # F4 (beat 4) — end of bar 2

    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),   # F4 (beat 1)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb4 (beat 2)
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Ab4 (beat 3)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A4 (beat 4) — variation, leading to Am7 chord

    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # A4 (beat 1)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Bb4 (beat 2)
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Ab4 (beat 3)
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # F4 (beat 4) — resolution
]

sax.notes = sax_notes

# Add the instruments to the MIDI
midi.instruments = [drums, bass, piano, sax]

# Write the MIDI file
# midi.write disabled

print("MIDI file generated: 'dante_intro.mid'")
