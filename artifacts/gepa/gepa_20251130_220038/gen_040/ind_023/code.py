
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F minor (Fm)
# The key is defined by the time signature and the instrument's tuning, but we'll just use F as the root.

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)  # Tenor Saxophone
bass_instrument = pretty_midi.Instrument(program=33)  # Upright Bass
piano_instrument = pretty_midi.Instrument(program=0)   # Acoustic Piano
drums_instrument = pretty_midi.Instrument(program=0)   # Drums

# Add instruments to the piece
pm.instruments.append(sax_instrument)
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drums_instrument)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# BPM: 160
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Note durations in beats (each beat = 0.375 seconds at 160 BPM)
beat = 0.375

# Bar 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Drums: Kick on 1, 3; Snare on 2, 4; Hihat on every eighth
for bar in range(1):
    for i in range(8):  # 8 eighth notes per bar
        time = bar * 1.5 + i * beat * 0.5
        if i % 2 == 0:  # Hihat on every eighth
            pm.instruments[-1].notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05))
        if i == 0:  # Kick on 1
            pm.instruments[-1].notes.append(pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.1))
        if i == 1:  # Snare on 2
            pm.instruments[-1].notes.append(pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.1))
        if i == 3:  # Kick on 3
            pm.instruments[-1].notes.append(pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.1))
        if i == 4:  # Snare on 4
            pm.instruments[-1].notes.append(pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.1))

# Bar 2: Everyone comes in
# Bass: Walking line, chromatic approaches, no repeated notes
# Fm key: F, Ab, Bb, C, Eb, G, A (we’ll use Fm7: F, Ab, Bb, D)

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.5 + 0.25),  # F (root)
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=1.75 + 0.25), # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.0 + 0.25),  # D (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.25 + 0.25), # Bb (3rd)
]
bass_instrument.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4 (Fm7: F, Ab, Bb, D)
piano_notes = [
    # Bar 2, measure 1, beat 2: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=1.75 + 0.1), # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=1.75 + 0.1), # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=1.75 + 0.1), # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.75 + 0.1), # D
    # Bar 2, measure 1, beat 4: Fm7 again
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.25 + 0.1), # F
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.25 + 0.1), # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.25 + 0.1), # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.25 + 0.1), # D
]
piano_instrument.notes.extend(piano_notes)

# Saxophone: 4-bar melody (bars 2-4), sparse, expressive
# Melody: Fm key, sparse, emotional, sparse phrasing

# Bar 2 - Start the motif (fragment)
# F (65) - whisper
pm.instruments[0].notes.append(pretty_midi.Note(velocity=60, pitch=65, start=1.5, end=1.5 + 0.3))
# A (69) - slight tension
pm.instruments[0].notes.append(pretty_midi.Note(velocity=70, pitch=69, start=1.8, end=1.8 + 0.25))
# Bb (60) - resolution
pm.instruments[0].notes.append(pretty_midi.Note(velocity=75, pitch=60, start=2.05, end=2.05 + 0.3))

# Bar 3 - Continue the motif (develop it)
# Ab (63) - descending line
pm.instruments[0].notes.append(pretty_midi.Note(velocity=70, pitch=63, start=3.0, end=3.0 + 0.25))
# F (65) - return
pm.instruments[0].notes.append(pretty_midi.Note(velocity=75, pitch=65, start=3.25, end=3.25 + 0.3))
# Eb (62) - tension again
pm.instruments[0].notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.6, end=3.6 + 0.25))

# Bar 4 - Resolve the motif (emotional release)
# D (62) - build
pm.instruments[0].notes.append(pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.5 + 0.25))
# F (65) - return, but louder
pm.instruments[0].notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=4.75 + 0.35))
# Silence on the last note, let the air hang

# Save the MIDI file
pm.write("Fm_intro.mid")
