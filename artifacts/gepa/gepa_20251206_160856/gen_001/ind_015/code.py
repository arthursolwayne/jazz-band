
import pretty_midi

# Setup
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Set key: D minor (Dm)
key = 'Dm'

# Time parameters
bpm = 160
ticks_per_beat = 480
time_per_beat = 60.0 / bpm
time_per_bar = time_per_beat * 4

# Instrument tracks
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# 1. BASS LINE - Marcus (Walking line, D2-G2, root and fifth with chromatic approaches)

# Bar 1: Dm (D, F, A, C) -> Dm7 -> Dm -> Dm7
bass_notes = [
    # Bar 1 (Dm7) - D2 (D), F (F), A (A), C (C)
    pretty_midi.Note(velocity=100, pitch=62, start=0.0, end=0.375),  # D2
    pretty_midi.Note(velocity=90, pitch=67, start=0.0, end=0.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=0.0, end=0.375),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=0.0, end=0.375),  # C
    # Bar 2 (Dm7) - D2, F, Bb (chromatic approach), A
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=70, start=1.5, end=1.875),  # Bb (chromatic)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A
    # Bar 3 (Dm7) - D2, F, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # C
    # Bar 4 (Dm7) - D2, F, Bb (chromatic approach), A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=70, pitch=70, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # A
]
bass.notes.extend(bass_notes)

# 2. PIANO - Diane (Open voicings, unique chords, comp on 2 and 4)

# Bar 1 (Dm7) - No chord (wait)
# Bar 2 (Dm7) - Open voicing: Dm7 (D, F, A, C)
piano_notes = [
    # Bar 2 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=70, pitch=67, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=70, pitch=67, start=1.5, end=1.875),  # C
    # Bar 3 (Dm7) - Dm7 with extension (D, F, A, C, G)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=70, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=70, pitch=67, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=60, pitch=76, start=3.0, end=3.375),  # G
    # Bar 4 (Dm7) - Dm7 with altered chord (Dm7b5)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=70, pitch=67, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=70, pitch=71, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=70, pitch=64, start=4.5, end=4.875),  # Eb (b5)
]
piano.notes.extend(piano_notes)

# 3. DRUMS - Little Ray (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)

# Bar 1: Drums only
drum_notes = [
    # Kick on 1 and 3 (Bar 1)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 3
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),   # 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375), # 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625), # 3
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),  # 4
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),  # 5
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125), # 6
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125), # 7
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),   # 8
    # Repeat for Bar 2 (same pattern)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),   # 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875), # 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625), # 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),  # 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),  # 5
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625), # 6
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125), # 7
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),   # 8
    # Bar 3 (same pattern)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),   # 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375), # 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625), # 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),  # 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),  # 5
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125), # 6
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125), # 7
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),   # 8
]
drums.notes.extend(drum_notes)

# 4. SAX - Dante (Motif: One short phrase, start it, leave it hanging, come back)

# Motif: A simple, haunting phrase in D minor that lingers.
# Example: D (E) -> F (D) -> A (B) -> C (D)
# (Play D, F, A, C with slight chromatic inflection, and then repeat the motif an octave higher)

sax_notes = [
    # Bar 2 - Start the motif (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # C
    # Bar 3 - Repeat the motif an octave higher
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # D (octave)
    pretty_midi.Note(velocity=100, pitch=77, start=3.25, end=3.5),  # F (octave)
    pretty_midi.Note(velocity=100, pitch=81, start=3.5, end=3.75),  # A (octave)
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.0),  # C (octave)
]
sax.notes.extend(sax_notes)

# Write MIDI file
pm.write('dante_intro.mid')
print("MIDI file written to 'dante_intro.mid'")
