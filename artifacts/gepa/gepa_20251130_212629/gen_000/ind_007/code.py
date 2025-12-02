
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
# Bars 2 and 4: D7, G7, C7
piano_notes = [
    # Bar 2: D7
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875), # D
    # Bar 3: comp
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=86, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=89, start=2.25, end=2.625), # G
    # Bar 4: G7
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=90, pitch=86, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=89, start=3.0, end=3.375), # F
    # Bar 5: comp
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=86, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=89, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=92, start=3.75, end=4.125), # G
    # Bar 6: C7
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875), # B
    # Bar 7: comp
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=84, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=90, pitch=89, start=5.25, end=5.625), # D
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 7):
    # Bar start
    bar_start = i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0)

# Saxophone (Dante) - motif in D
# Start with a phrase that sings, then leave it hanging, then come back to finish it
# Motif: D (E) F# G (A) G F# D
# Note durations: 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=2.0),    # D
    pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.25),   # E
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.5),   # F#
    pretty_midi.Note(velocity=110, pitch=79, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=110, pitch=81, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=110, pitch=79, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.5),   # F#
    pretty_midi.Note(velocity=110, pitch=74, start=3.5, end=3.75),   # D
    # Then leave it hanging
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=110, pitch=76, start=4.0, end=4.25),   # E
    pretty_midi.Note(velocity=110, pitch=77, start=4.25, end=4.5),   # F#
    pretty_midi.Note(velocity=110, pitch=79, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=110, pitch=81, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=110, pitch=79, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=110, pitch=77, start=5.25, end=5.5),   # F#
    pretty_midi.Note(velocity=110, pitch=74, start=5.5, end=6.0),    # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
