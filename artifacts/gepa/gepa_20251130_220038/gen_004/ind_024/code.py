
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),# Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Sax, Bass, Piano join
# Sax - motif: F, Bb, D, G (F7 chord, descending)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # G
]
sax.notes.extend(sax_notes)

# Bass - walking line: F, G, Ab, A, Bb, B, C, D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5), # D
]
bass.notes.extend(bass_notes)

# Piano - F7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25), # F (root)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # A (7th)
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25), # C (3rd)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # E (5th)
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75), # F (root)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # A (7th)
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75), # C (3rd)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # E (5th)
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues motif, Bass continues, Piano fills in
# Sax - repeat motif but shift to Bb7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5), # G
]
sax.notes.extend(sax_notes)

# Bass - walking line: Bb, C, C#, D, Eb, E, F, G
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # C#
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0), # G
]
bass.notes.extend(bass_notes)

# Piano - Bb7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75), # Bb (root)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # D (7th)
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75), # F (3rd)
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75), # G (5th)
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # Bb (root)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # D (7th)
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25), # F (3rd)
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25), # G (5th)
]
piano.notes.extend(piano_notes)

# Bar 4: Sax finishes motif, Bass continues, Piano fills in
# Sax - finish motif with F and resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F
]
sax.notes.extend(sax_notes)

# Bass - walking line: F, G, Ab, A, Bb, B, C, D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0), # A
]
bass.notes.extend(bass_notes)

# Piano - F7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25), # F (root)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # A (7th)
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # C (3rd)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # E (5th)
]
piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
