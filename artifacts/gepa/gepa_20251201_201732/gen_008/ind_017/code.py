
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare on 4
]
for i in range(4):
    pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=(i+1)*0.375).add_to_instrument(drums)

for note in drum_notes:
    note.add_to_instrument(drums)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=2.0), # F2
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.5), # G2
    pretty_midi.Note(velocity=90, pitch=39, start=2.5, end=3.0), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.5), # C3 (fifth of F)
    pretty_midi.Note(velocity=90, pitch=41, start=3.5, end=4.0), # A2
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.5), # C3
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=5.0), # B2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=47, start=5.0, end=5.5), # F3 (octave)
    pretty_midi.Note(velocity=90, pitch=45, start=5.5, end=6.0), # D3
]

for note in bass_notes:
    note.add_to_instrument(bass)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0), # E
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.0), # G
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=2.0), # C
]

# Bar 3: Bm7b5 (B, D, F, A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.5), # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.5), # C#
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.5), # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5), # F#
])

# Bar 4: D7 (D, F#, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=3.0), # C#
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0), # F#
])

# Bar 4: F7 (F, A, C, E)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.5), # E
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.5), # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.5), # A
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.5), # C
])

# Bar 4: Fmaj7 (F, A, C, E)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=4.0), # E
    pretty_midi.Note(velocity=90, pitch=55, start=3.5, end=4.0), # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=4.0), # A
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=4.0), # C
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.5), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.5), # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.5), # F
])

# Bar 4: Fmaj7 (F, A, C, E)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=5.0), # E
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=5.0), # G
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=5.0), # A
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=5.0), # C
])

# Bar 4: Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=57, start=5.0, end=5.5), # A
    pretty_midi.Note(velocity=90, pitch=59, start=5.0, end=5.5), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.5), # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.5), # E
])

# Bar 4: F7 (F, A, C, E)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=5.5, end=6.0), # E
    pretty_midi.Note(velocity=90, pitch=55, start=5.5, end=6.0), # G
    pretty_midi.Note(velocity=90, pitch=57, start=5.5, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=59, start=5.5, end=6.0), # C
])

for note in piano_notes:
    note.add_to_instrument(piano)

# Sax: Motif, start it, leave it hanging, come back and finish it
# F (59) -> A (62) -> F (59) -> C (60)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0), # A
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75), # C
]

for note in sax_notes:
    note.add_to_instrument(sax)

# Drums: continue pattern
for i in range(4, 8):
    pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=(i+1)*0.375).add_to_instrument(drums)

# Final kick and snare on bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.375, end=5.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.75, end=6.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.125, end=6.5), # Snare on 4
]

for note in drum_notes:
    note.add_to_instrument(drums)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
