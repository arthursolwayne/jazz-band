
import pretty_midi

# Create a PrettyMIDI object at 160 BPM in F major
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax (MIDI program 64)
pm.instruments.append(instrument)

# Define the time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Time per beat at 160 BPM = 0.375 seconds
# 4 bars = 6.0 seconds
# Bar 1: 0.0 to 1.5 seconds (Little Ray only)
# Bar 2-4: 1.5 to 6.0 seconds (Full ensemble)

# ---------- BAR 1: Little Ray (Drums) -------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time grid for bar 1 (1.5 seconds)
# 0.0, 0.375 (1), 0.75 (2), 1.125 (3), 1.5 (4)

# Kick on 1 and 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.1),
              pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.85)]

# Snare on 2 and 4
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.45),
               pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.225)]

# Hi-hat on every eighth
hihat_notes = [pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.075),
               pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.45),
               pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.825),
               pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.2),
               pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.575)]

# Add to drum instrument (program 49)
drum_instrument = pretty_midi.Instrument(program=49)
drum_instrument.notes.extend(kick_notes)
drum_instrument.notes.extend(snare_notes)
drum_instrument.notes.extend(hihat_notes)
pm.instruments.append(drum_instrument)

# ------------------ BAR 2-4: Full Ensemble --------------------

# Time starts at 1.5s for Bar 2

# ------------------ Marcus (Bass) ----------------------------
# Walking line with chromatic approaches, never repeating a note
# Use F as root, with chromatic passing tones

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.6),     # F (root)
    pretty_midi.Note(velocity=80, pitch=49, start=1.6, end=1.7),     # Gb (chromatic)
    pretty_midi.Note(velocity=80, pitch=50, start=1.7, end=1.8),     # G (3rd)
    pretty_midi.Note(velocity=80, pitch=51, start=1.8, end=1.9),     # Ab (chromatic)
    pretty_midi.Note(velocity=80, pitch=52, start=1.9, end=2.0),     # A (5th)
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.1),     # Bb (chromatic)
    pretty_midi.Note(velocity=80, pitch=54, start=2.1, end=2.2),     # B (7th)
    pretty_midi.Note(velocity=80, pitch=55, start=2.2, end=2.3),     # C (octave)
    pretty_midi.Note(velocity=80, pitch=56, start=2.3, end=2.4),     # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=55, start=2.4, end=2.5),     # C (back down)
    pretty_midi.Note(velocity=80, pitch=54, start=2.5, end=2.6),     # B
    pretty_midi.Note(velocity=80, pitch=53, start=2.6, end=2.7),     # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=2.7, end=2.8),     # A
    pretty_midi.Note(velocity=80, pitch=51, start=2.8, end=2.9),     # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=2.9, end=3.0),     # G
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.1),     # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=3.1, end=3.2),     # F
]

# Add to bass (program 33)
bass_instrument = pretty_midi.Instrument(program=33)
bass_instrument.notes.extend(bass_notes)
pm.instruments.append(bass_instrument)

# ------------------ Diane (Piano) ----------------------------
# 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# 2nd beat (1.875s): F7
# 4th beat (3.375s): F7

chord_notes_2 = [pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),  # F
                 pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.0),  # A
                 pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # C
                 pretty_midi.Note(velocity=100, pitch=56, start=1.875, end=2.0)]  # Eb

chord_notes_4 = [pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.575),
                 pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.575),
                 pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.575),
                 pretty_midi.Note(velocity=100, pitch=56, start=3.375, end=3.575)]

# Add to piano (program 0)
piano_instrument = pretty_midi.Instrument(program=0)
piano_instrument.notes.extend(chord_notes_2)
piano_instrument.notes.extend(chord_notes_4)
pm.instruments.append(piano_instrument)

# ------------------ Dante (Tenor Sax) ----------------------------
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Start at 1.5s
# Notes: F (48), G (50), Bb (52), F (48)
# Let it hang on the Bb

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.75, end=1.9),  # G
    pretty_midi.Note(velocity=110, pitch=52, start=1.9, end=2.4),   # Bb (hang for 0.5s)
    pretty_midi.Note(velocity=110, pitch=48, start=2.4, end=2.6),   # F (return)
    pretty_midi.Note(velocity=110, pitch=50, start=2.6, end=2.8),   # G
    pretty_midi.Note(velocity=110, pitch=52, start=2.8, end=3.0)    # Bb (end on a question)
]

# Add to sax
sax_instrument = pretty_midi.Instrument(program=64)
sax_instrument.notes.extend(sax_notes)
pm.instruments.append(sax_instrument)

# ------------------ Little Ray (Drums) for Bar 2-4 --------------------

# Keep the same pattern for the next 3 bars

# Kick on 1 and 3
kick_notes_2 = [pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6),
                pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.35),
                pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1),
                pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.85)]

# Snare on 2 and 4
snare_notes_2 = [pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=1.975),
                 pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.725),
                 pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.475),
                 pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.225)]

# Hi-hat on every eighth
hihat_notes_2 = [pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.575),
                 pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=1.95),
                 pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.325),
                 pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.7),
                 pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.075),
                 pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.45),
                 pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.825),
                 pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.2)]

# Add to drum instrument
drum_instrument.notes.extend(kick_notes_2)
drum_instrument.notes.extend(snare_notes_2)
drum_instrument.notes.extend(hihat_notes_2)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
