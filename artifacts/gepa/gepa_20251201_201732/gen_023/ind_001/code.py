
import pretty_midi
from pretty_midi import PrettyMIDI, Instrument, Note

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_instrument = Instrument(program=33)  # Electric Bass
piano_instrument = Instrument(program=0)  # Acoustic Piano
drums_instrument = Instrument(program=0)  # Drums
sax_instrument = Instrument(program=64)  # Tenor Sax

# Add instruments to the PrettyMIDI object
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drums_instrument)
pm.instruments.append(sax_instrument)

# Time divisions (for 160 BPM, 4/4 time, 6 seconds for 4 bars)
time_per_beat = 60.0 / 160.0  # seconds per beat
time_per_bar = 4 * time_per_beat  # 4 beats per bar
total_time = 4 * time_per_bar  # 4 bars = 6 seconds

# --- DRUMS: Bar 1 (0-1.5s) ---
# Little Ray: roll on snare and toms to build tension
drum_notes = [
    # Snare roll on 16th notes
    Note(velocity=70, start=0.0, end=0.05, pitch=38),
    Note(velocity=70, start=0.05, end=0.1, pitch=38),
    Note(velocity=70, start=0.1, end=0.15, pitch=38),
    Note(velocity=70, start=0.15, end=0.2, pitch=38),
    Note(velocity=70, start=0.2, end=0.25, pitch=38),
    Note(velocity=70, start=0.25, end=0.3, pitch=38),
    Note(velocity=70, start=0.3, end=0.35, pitch=38),
    Note(velocity=70, start=0.35, end=0.4, pitch=38),
    # Toms
    Note(velocity=60, start=0.1, end=0.12, pitch=64),
    Note(velocity=60, start=0.25, end=0.27, pitch=64),
    Note(velocity=60, start=0.4, end=0.42, pitch=64),
]

drums_instrument.notes.extend(drum_notes)

# --- PIANO: Bar 2 (1.5-3.0s) ---
# Diane: open voicings, different chords each bar, comp on 2 and 4
# Bar 2: C7 (Fmaj7) -> F, A, C, E, G
note1 = Note(velocity=80, start=1.5, end=1.6, pitch=72)  # F
note2 = Note(velocity=80, start=1.5, end=1.6, pitch=76)  # A
note3 = Note(velocity=80, start=1.5, end=1.6, pitch=79)  # C
note4 = Note(velocity=80, start=1.5, end=1.6, pitch=82)  # E
note5 = Note(velocity=80, start=1.5, end=1.6, pitch=84)  # G
piano_instrument.notes.extend([note1, note2, note3, note4, note5])

# Bar 3: Gm7 (Fmaj7 -> Gm7) -> G, Bb, D, F
note1 = Note(velocity=80, start=3.0, end=3.1, pitch=78)  # G
note2 = Note(velocity=80, start=3.0, end=3.1, pitch=80)  # Bb
note3 = Note(velocity=80, start=3.0, end=3.1, pitch=82)  # D
note4 = Note(velocity=80, start=3.0, end=3.1, pitch=84)  # F
piano_instrument.notes.extend([note1, note2, note3, note4])

# Bar 4: Am7 (Fmaj7 -> Am7) -> A, C, E, G
note1 = Note(velocity=80, start=4.5, end=4.6, pitch=79)  # A
note2 = Note(velocity=80, start=4.5, end=4.6, pitch=81)  # C
note3 = Note(velocity=80, start=4.5, end=4.6, pitch=84)  # E
note4 = Note(velocity=80, start=4.5, end=4.6, pitch=86)  # G
piano_instrument.notes.extend([note1, note2, note3, note4])

# --- BASS: Walking line in F (D2-G2, MIDI 38-43)
# Bar 2: F -> G -> A -> Bb
note1 = Note(velocity=80, start=1.5, end=1.6, pitch=38)  # F
note2 = Note(velocity=80, start=1.6, end=1.7, pitch=40)  # G
note3 = Note(velocity=80, start=1.7, end=1.8, pitch=42)  # A
note4 = Note(velocity=80, start=1.8, end=1.9, pitch=43)  # Bb
bass_instrument.notes.extend([note1, note2, note3, note4])

# Bar 3: Bb -> C -> D -> E
note1 = Note(velocity=80, start=3.0, end=3.1, pitch=43)  # Bb
note2 = Note(velocity=80, start=3.1, end=3.2, pitch=45)  # C
note3 = Note(velocity=80, start=3.2, end=3.3, pitch=47)  # D
note4 = Note(velocity=80, start=3.3, end=3.4, pitch=49)  # E
bass_instrument.notes.extend([note1, note2, note3, note4])

# Bar 4: E -> F -> G -> A
note1 = Note(velocity=80, start=4.5, end=4.6, pitch=49)  # E
note2 = Note(velocity=80, start=4.6, end=4.7, pitch=50)  # F
note3 = Note(velocity=80, start=4.7, end=4.8, pitch=52)  # G
note4 = Note(velocity=80, start=4.8, end=4.9, pitch=54)  # A
bass_instrument.notes.extend([note1, note2, note3, note4])

# --- SAX: Your motif (Bar 2-4)
# You: Searching, then finding
# Bar 2: F - A - Bb - D
note1 = Note(velocity=90, start=1.5, end=1.625, pitch=72)  # F
note2 = Note(velocity=90, start=1.625, end=1.75, pitch=76)  # A
note3 = Note(velocity=90, start=1.75, end=1.875, pitch=77)  # Bb
note4 = Note(velocity=90, start=1.875, end=2.0, pitch=82)  # D
sax_instrument.notes.extend([note1, note2, note3, note4])

# Bar 3: Repeat but altered
note1 = Note(velocity=90, start=3.0, end=3.125, pitch=72)  # F
note2 = Note(velocity=90, start=3.125, end=3.25, pitch=76)  # A
note3 = Note(velocity=90, start=3.25, end=3.375, pitch=77)  # Bb
note4 = Note(velocity=90, start=3.375, end=3.5, pitch=82)  # D
sax_instrument.notes.extend([note1, note2, note3, note4])

# Bar 4: Resolving
note1 = Note(velocity=90, start=4.5, end=4.625, pitch=72)  # F
note2 = Note(velocity=90, start=4.625, end=4.75, pitch=76)  # A
note3 = Note(velocity=90, start=4.75, end=4.875, pitch=77)  # Bb
note4 = Note(velocity=90, start=4.875, end=5.0, pitch=81)  # C
sax_instrument.notes.extend([note1, note2, note3, note4])

# Write to file
pm.write('jazz_intro_f_major.mid')
print("MIDI file saved as 'jazz_intro_f_major.mid'")
