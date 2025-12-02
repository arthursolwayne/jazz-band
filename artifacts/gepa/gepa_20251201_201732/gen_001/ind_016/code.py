
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (D2 is MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # D#2 on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0), # G2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875), # C4
]
piano.notes.extend(piano_notes)

# Sax: Motif - Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0), # F#4
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0), # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (D2 is MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # G2 on 1
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # F2 on 2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # Eb2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5), # D2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B D F# A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375), # A4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375), # D4
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation - Resolve the phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75), # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5), # A4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (D2 is MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875), # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625), # D#2 on 3
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0), # G2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875), # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875), # F4
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution - Complete the phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25), # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0), # B4
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375), # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
